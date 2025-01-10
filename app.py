import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
from datetime import datetime, timedelta
import copy
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    time = 0
    schedule = []

    for process in processes:
        if time < process['arrival_time']:
            time = process['arrival_time']
        start_time = time
        completion_time = start_time + process['burst_time']
        time = completion_time

        schedule.append({
            'process': process['id'],
            'start_time': start_time,
            'completion_time': completion_time
        })

    return schedule


def non_preemptive_sjf(processes):
    processes = processes[:]
    processes.sort(key=lambda x: x['arrival_time'])
    time = 0
    schedule = []

    while processes:
        available = [p for p in processes if p['arrival_time'] <= time]
        if available:
            next_process = min(available, key=lambda x: x['burst_time'])
            processes.remove(next_process)
            start_time = max(time, next_process['arrival_time'])
            completion_time = start_time + next_process['burst_time']
            time = completion_time
            schedule.append({
                'process': next_process['id'],
                'start_time': start_time,
                'completion_time': completion_time
            })
        else:
            time += 1
    return schedule


def preemptive_sjf(processes):
    processes = copy.deepcopy(processes)
    processes = sorted(processes, key=lambda x: x['arrival_time'])
    time = 0
    schedule = []
    remaining_processes = processes[:]
    
    while remaining_processes:
        available = [p for p in remaining_processes if p['arrival_time'] <= time]

        if available:
            available.sort(key=lambda x: (x['burst_time'], x['arrival_time']))
            current_process = available[0]

            if not schedule or schedule[-1]['process'] != current_process['id']:
                if schedule and 'completion_time' not in schedule[-1]:
                    schedule[-1]['completion_time'] = time
                schedule.append({'process': current_process['id'], 'start_time': time})

            current_process['burst_time'] -= 1
            time += 1

            if current_process['burst_time'] == 0:
                schedule[-1]['completion_time'] = time
                remaining_processes.remove(current_process)
        else:
            if not schedule or schedule[-1]['process'] != 'idle':
                schedule.append({'process': 'idle', 'start_time': time})
            time += 1
            if schedule[-1]['process'] == 'idle':
                schedule[-1]['completion_time'] = time

    return schedule



def round_robin(processes, time_quantum):
    queue = sorted(processes, key=lambda x: x['arrival_time'])
    time = 0
    schedule = []

    while queue:
        current = queue.pop(0)
        if current['arrival_time'] > time:
            time = current['arrival_time']

        start_time = time
        execution_time = min(time_quantum, current['burst_time'])
        current['burst_time'] -= execution_time
        time += execution_time

        schedule.append({
            'process': current['id'],
            'start_time': start_time,
            'completion_time': time
        })

        if current['burst_time'] > 0:
            queue.append(current)

    return schedule


def priority_scheduling(processes):
    processes=processes[:]
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))
    time = 0
    schedule = []

    while processes:
        available = [p for p in processes if p['arrival_time'] <= time]
        if available:
            next_process = min(available, key=lambda x: x['priority'])
            processes.remove(next_process)
            start_time = max(time, next_process['arrival_time'])
            completion_time = start_time + next_process['burst_time']
            time = completion_time
            schedule.append({
                'process': next_process['id'],
                'start_time': start_time,
                'completion_time': completion_time
            })
        else:
            time += 1

    return schedule

def calculate_metrics(processes, schedule):
    waiting_time = {}
    turnaround_time = {}
    response_time = {}
    start_times = {}

    for process in schedule:
        pid = process['process']
        if pid not in start_times:
            start_times[pid] = process['start_time']

        completion_time = process['completion_time']
        arrival_time = next(p['arrival_time'] for p in processes if p['id'] == pid)
        burst_time = next(p['burst_time'] for p in processes if p['id'] == pid)

        turnaround_time[pid] = completion_time - arrival_time
        waiting_time[pid] = turnaround_time[pid] - burst_time

    for pid, start_time in start_times.items():
        arrival_time = next(p['arrival_time'] for p in processes if p['id'] == pid)
        response_time[pid] = start_time - arrival_time

    avg_waiting_time = sum(waiting_time.values()) / len(processes)
    avg_turnaround_time = sum(turnaround_time.values()) / len(processes)
    avg_response_time = sum(response_time.values()) / len(processes)
    return avg_waiting_time, avg_turnaround_time, avg_response_time

def plot_gantt_chart(schedule):
    tasks = []
    start_reference = datetime(2025, 1, 1)
    
    for item in schedule:
        start_time = start_reference + timedelta(seconds=item['start_time'])
        finish_time = start_reference + timedelta(seconds=item['completion_time'])
        tasks.append(dict(
            Task=f"Process {item['process']}",
            Start=start_time,
            Finish=finish_time
        ))

    fig = ff.create_gantt(tasks, show_colorbar=True, index_col="Task", group_tasks=True)
    st.plotly_chart(fig)

st.set_page_config(page_title="CPU Scheduling Algorithms",layout='wide')
st.title("⚙️CPU Scheduling Algorithms")

st.sidebar.header("Input Parameters")
algorithm = st.sidebar.selectbox(
    "Choose Scheduling Algorithm",
    [
        "First Come First Serve (FCFS)",
        "Non-Preemptive SJF",
        "Preemptive SJF",
        "Round Robin",
        "Priority Scheduling"
    ]
)

num_processes = st.sidebar.number_input("Number of Processes", min_value=1, value=3)

time_quantum = None
if algorithm == "Round Robin":
    time_quantum = st.sidebar.number_input("Time Quantum", min_value=1, value=2)

process_data = []
for i in range(num_processes):
    with st.sidebar.expander(f"Process {i+1}"):
        pid = i + 1
        arrival_time = st.number_input(f"Arrival Time (P{pid})", min_value=0, key=f"arrival_{pid}")
        burst_time = st.number_input(f"Burst Time (P{pid})", min_value=1, key=f"burst_{pid}")
        priority = None
        if algorithm == "Priority Scheduling":
            priority = st.number_input(f"Priority (P{pid})", min_value=1, key=f"priority_{pid}")
        process_data.append({'id': pid, 'arrival_time': arrival_time, 'burst_time': burst_time, 'priority': priority})

if st.sidebar.button("Run Scheduling"):
    if process_data:
        st.subheader("Scheduling Results")
        if algorithm == "First Come First Serve (FCFS)":
            result = fcfs_scheduling(process_data)
        elif algorithm == "Non-Preemptive SJF":
            result = non_preemptive_sjf(process_data)
        elif algorithm == "Preemptive SJF":
            result = preemptive_sjf(process_data)
        elif algorithm == "Round Robin":
            result = round_robin(process_data, time_quantum)
        elif algorithm == "Priority Scheduling":
            result = priority_scheduling(process_data)

        df = pd.DataFrame(result)
        st.write(df)
        
        st.subheader("📊Gantt Chart")
        plot_gantt_chart(result)
        avg_waiting_time, avg_turnaround_time, avg_response_time = calculate_metrics(process_data, result)

        st.subheader("Performance Metrics")
        st.write(f"**Average Waiting Time**: {avg_waiting_time:.2f}")
        st.write(f"**Average Turnaround Time**: {avg_turnaround_time:.2f}")
        st.write(f"**Average Response Time**: {avg_response_time:.2f}")