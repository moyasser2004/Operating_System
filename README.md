# CPU Scheduling Algorithms

## Project Overview
This project focuses on implementing and analyzing various CPU scheduling algorithms used in operating systems. CPU scheduling is a crucial aspect of process management, determining the order in which processes are executed by the CPU to optimize performance and resource utilization.

## Key Features

### 1. **Implemented Algorithms**
- **First-Come, First-Served (FCFS)**:
  - Non-preemptive algorithm.
  - Processes are executed in the order they arrive.
- **Shortest Job Next (SJN)**:
  - Non-preemptive algorithm.
  - Processes with the shortest burst time are executed first.
- **Priority Scheduling**:
  - Can be preemptive or non-preemptive.
  - Processes are scheduled based on priority.
- **Round Robin (RR)**:
  - Preemptive algorithm.
  - Each process gets a fixed time slice (quantum) in a cyclic order.
- **Multilevel Queue Scheduling**:
  - Processes are divided into multiple queues based on priority.
  - Each queue has its own scheduling policy.

### 2. **Simulation and Analysis**
- Simulates the behavior of each scheduling algorithm with user-defined processes.
- Calculates and compares key performance metrics:
  - Average waiting time.
  - Average turnaround time.
  - CPU utilization.
  - Throughput.

### 3. **Interactive User Interface**
- Allows users to input process details such as arrival time, burst time, and priority.
- Visual representation of the Gantt chart for each algorithm.
- Displays detailed statistics for analysis.

## Technologies Used

### Programming Languages:
- **Python**: Core language for simulation and analysis.

### Libraries and Tools:
- **Tkinter** or **PyQt**: For creating the graphical user interface (optional).
- **Matplotlib**: For visualizing Gantt charts and performance comparisons.
- **Pandas**: For data manipulation and analysis.

## Installation and Setup

### Prerequisites:
1. Python 3.8 or higher.
2. pip (Python package manager).

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cpu-scheduling-algorithms.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cpu-scheduling-algorithms
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the simulation:
   ```bash
   python main.py
   ```

## Usage
1. **Input Process Details**:
   - Enter the arrival time, burst time, and priority (if applicable) for each process.

2. **Select Algorithm**:
   - Choose a scheduling algorithm to simulate.

3. **View Results**:
   - Observe the Gantt chart and performance metrics for the selected algorithm.

4. **Compare Algorithms**:
   - Run simulations for different algorithms and compare their metrics.

## Future Enhancements
- **Dynamic Process Addition**: Allow processes to be added during runtime.
- **Customizable Quantum**: Let users modify the time quantum for Round Robin scheduling.
- **Multilevel Feedback Queue**: Implement advanced scheduling algorithms.
- **Real-Time Scheduling**: Extend the project to include real-time scheduling techniques.

## Contributing
Contributions are welcome! If you'd like to improve this project, please:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

---
Feel free to reach out for support or provide feedback to improve this project!

