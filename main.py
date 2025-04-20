workout_plan = {
    "Push-ups": {
        "sets": 3,
        "reps": 15,
        "notes": "Keep your back straight, hands shoulder-width apart."
    },
    "Squats": {
        "sets": 4,
        "reps": 12,
        "notes": "Go as low as you can while maintaining proper form."
    },
    "Plank": {
        "sets": 3,
        "reps": "Hold for 60 seconds",
        "notes": "Engage your core and keep your body in a straight line."
    },
    "Lunges": {
        "sets": 3,
        "reps": 10,
        "notes": "Each leg. Step forward and lower your body until your front knee is at a 90-degree angle."
    },
    "Bicep Curls": {
        "sets": 3,
        "reps": 12,
        "notes": "Use dumbbells, keep your elbows close to your body."
    }
}


print(workout_plan["Push-ups"]["sets"])
print(workout_plan["Push-ups"]["reps"])
print(workout_plan["Push-ups"]["notes"])

# Modifying the sets and notes
workout_plan["Push-ups"]["sets"] = 12
del workout_plan["Push-ups"]["notes"]

# Adding a new note
workout_plan["Push-ups"]["workout_notes"] = "Keep your back straight, legs apart and straight."

print(workout_plan)

#iterating over a disctinary
for key, value in workout_plan["Plank"].items():
    print(f"{key.upper()}: {value}")
