# Job-Scheduler
to schedule jobs and assign workers in an optimal way
Assumptions

Objectives
    we want to maximize the number of jobs the company can cover at any given schedule period
    we want to minimize the travel time between jobs for each worker
    (do we) want to assign workers to jobs in a uniform way meaning the variance of average working hours per worker per schedule period (or per day) is minimum 

Scheduling a job for the customer
    each job has a given location
    the jobs are scheduled based on the availability times provided by the customer
    a Job may be an emergency ASAP job which is lost if not scheduled and assigned before a certain time window
    a job may be a one-off job or a recurring job
    a job may need a pre-requisite job to be completed before being scheduled e.g. an assessment 

Assigning Jobs to workers
    want to assign workers to jobs based on their skillset
    a job may need more than one worker at the same time. if a job needs multiple workers at separate times, we can break down the job to smaller pieces



Traveling between Jobs
    the travel time between jobs is variable and depends on the traffic conditions based on the depart time
    A job may need specific supplies to be done which a worker may have or may need to buy before starting the job
    (do?)) workers start their work-day from various locations

Workers weekly (schedule period) schedule
    Workers can work a maximum of maximum hours in a day
    there needs to be a minimum number of minimum rest hours between two shifts a worker works