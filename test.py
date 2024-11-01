from worker.tasks import execute_booking_creating_event

a = {'slot_id': 101, 'user_id': 15}
execute_booking_creating_event.apply_async(args=(a,))
