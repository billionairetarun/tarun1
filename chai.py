BEGIN MasalaChaiProcedure

    //  INITIALIZATION :
    CALL get_water_in_utensil(SAUCEPAN, 200ml)
    SENSE saucepan_location
    HAND_1: MOVE TO saucepan_location
    HAND_1: GRAB saucepan
    HAND_1: MOVE TO STOVE_BURNER
    HAND_1: RELEASE
    ACTUATE stove_power ON (HIGH)

    //  SPICE PREPARATION (PARALLEL) :
    SENSE ginger_location, mortar_pestle_location
    HAND_2: MOVE TO ginger_location
    HAND_2: GRAB ginger
    HAND_2: MOVE TO mortar_pestle_location
    HAND_2: RELEASE ginger
    
    HAND_2: GRAB PESTLE
    REPEAT 15 TIMES:
        HAND_2: MOVE VERTICAL_DOWN (Apply Pressure)
        HAND_2: MOVE VERTICAL_UP
    END REPEAT
    
    HAND_2: GRAB crushed_spices FROM mortar_pestle
    HAND_2: MOVE TO SAUCEPAN
    HAND_2: RELEASE crushed_spices

    // --- PHASE 3: INFUSION ---
    FOR EACH ingredient IN [TEA_LEAVES, SUGAR]:
        SENSE ingredient_location
        HAND_2: MOVE TO ingredient_location
        HAND_2: GRAB (Quantity: 2 tsp)
        HAND_2: MOVE TO SAUCEPAN
        HAND_2: RELEASE
    END FOR

    // Wait for boil using temperature sensors
    WHILE SENSOR.temperature(SAUCEPAN) < 100°C:
        CONTINUE_BOILING
    END WHILE

    //  DAIRY & FINISHING :
    SENSE milk_location
    HAND_1: MOVE TO milk_location
    HAND_1: GRAB milk_container
    HAND_1: POUR 100ml INTO SAUCEPAN
    HAND_1: RELEASE milk_container

    //  prevent overflow
    WHILE SENSOR.liquid_level(SAUCEPAN) < UPPER_LIMIT:
        SENSE foam_height
        IF foam_height IS RISING_RAPIDLY:
            WAIT 0.5 SECONDS
        END IF
    END WHILE
    
    ACTUATE stove_power OFF

    //  FILTRATION & SERVING :
    SENSE cup_location, strainer_location
    HAND_1: MOVE TO strainer_location
    HAND_1: GRAB strainer
    HAND_1: MOVE AND HOLD 2cm ABOVE cup_location
    
    HAND_2: MOVE TO SAUCEPAN
    HAND_2: GRAB handle
    HAND_2: TILT_POUR INTO cup_location THROUGH strainer
    
    HAND_2: RELEASE SAUCEPAN TO countertop
    HAND_1: RELEASE strainer TO sink

END MasalaChaiProcedure