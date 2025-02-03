from ortools.sat.python import cp_model
import numpy as np
import random

# Define workers with skillsets and shift constraints
workers = [
    {"name": "Alice", "skills": {"plumbing", "hvac"}, "max_hours": 8 * 60, "min_rest": 10 * 60},
    {"name": "Bob", "skills": {"electrical", "painting"}, "max_hours": 9 * 60, "min_rest": 12 * 60},
    {"name": "Charlie", "skills": {"landscaping", "tree care"}, "max_hours": 7 * 60, "min_rest": 10 * 60}
]

# Define jobs with various constraints
jobs = [
    {"id": 1, "location": (10, 5), "duration": 60, "skill_required": "plumbing", "priority": "normal", "prereq": None},  
    {"id": 2, "location": (15, 10), "duration": 90, "skill_required": "electrical", "priority": "high", "prereq": None},  
    {"id": 3, "location": (20, 8), "duration": 45, "skill_required": "painting", "priority": "normal", "prereq": 2},  
    {"id": 4, "location": (25, 12), "duration": 30, "skill_required": "hvac", "priority": "emergency", "prereq": None},  
]
base_location = (0, 0)  

# Travel time matrix (in minutes, variable based on departure time)
def generate_travel_times(num_jobs):
    return [[random.randint(10, 40) for _ in range(num_jobs + 1)] for _ in range(num_jobs + 1)]

travel_times = generate_travel_times(len(jobs))

# Create the CP-SAT model
model = cp_model.CpModel()

# Decision variables: job_assignment[w][j] = 1 if worker w is assigned to job j
job_assignment = {}
for w in range(len(workers)):
    for j in range(len(jobs)):
        job_assignment[w, j] = model.NewBoolVar(f'worker_{w}_job_{j}')

# Each job is assigned to exactly one qualified worker
for j, job in enumerate(jobs):
    model.Add(sum(job_assignment[w, j] for w, worker in enumerate(workers) if job['skill_required'] in worker['skills']) == 1)

# Each worker should not exceed max working hours
for w, worker in enumerate(workers):
    model.Add(sum(jobs[j]['duration'] * job_assignment[w, j] for j in range(len(jobs))) <= worker['max_hours'])

# Handle job dependencies (prerequisites must be completed first)
for job in jobs:
    if job['prereq']:
        model.Add(sum(job_assignment[w, job['id']-1] for w in range(len(workers))) <= sum(job_assignment[w, job['prereq']-1] for w in range(len(workers))))

# Minimize total travel time
model.Minimize(sum(travel_times[i+1][j+1] * job_assignment[w, j] 
                   for w in range(len(workers)) for i in range(len(jobs)) for j in range(len(jobs))))

# Solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Print results
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for w, worker in enumerate(workers):
        assigned_jobs = [jobs[j]['id'] for j in range(len(jobs)) if solver.Value(job_assignment[w, j]) == 1]
        print(f"Worker {worker['name']} assigned jobs: {assigned_jobs}")
else:
    print("No feasible solution found.")
