from services.monitor_service import monitor_application

result = monitor_application()

if result:
    print("SYSTEM HEALTH: OK")
else:
    print("SYSTEM HEALTH: FAILED")