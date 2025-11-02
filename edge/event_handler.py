   client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("📡 Intelligent event handler running...\n")

    try:
        while True:
            # Check for inactivity
            if system_state == "ACTIVE" and last_motion_time:
                if (datetime.now() - last_motion_time).total_seconds() > INACTIVITY_LIMIT:
                    system_state = "IDLE"
                    print("⚪ State changed: IDLE")
                    log_event("STATE: IDLE")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n🛑 Exiting gracefully.")
        client.loop_stop()

if __name__ == "__main__":
    main()



