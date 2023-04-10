import matplotlib.pyplot as plt
import seaborn as sns
"""columns in df ['student_ID', 'Total_Que', 'attemted', 'correct_ans', 'time_given',
       'time_taken', 'attempted_percentage', 'correct_percentage', 'accuracy',
       'efficiency', 'total_score', 'score_percentage']"""




def weekly_perfo_graph():
    
    plt.plot([1,2,3,4,5,6,7],list_of_performence_weekly,color="r")
    plt.xlabel("week")
    plt.ylabel("Performence)
    plt.title("Weekly peformence")
               
def plot_student_performance(df, student_id):
    # filter the data frame to get the data for the specified student ID
    student_data = df[df['student_ID'] == student_id].iloc[0]
    
    # create a bar plot of the number of attempted and correct questions
    fig, ax = plt.subplots()
    ax.bar(['Attempted', 'Correct'], [student_data['attemted'], student_data['correct_ans']])
    ax.set_title(f'Student {student_id} Performance')
    ax.set_xlabel('Questions')
    ax.set_ylabel('Count')
    plt.show()
    
    # create a pie chart of the attempted vs. correct questions
    fig, ax = plt.subplots()
    ax.pie([student_data['correct_ans'], student_data['attemted'] - student_data['correct_ans']], 
           labels=['Correct', 'Incorrect'], autopct='%1.1f%%')
    ax.set_title(f'Student {student_id} Performance')
    plt.show()
    
    
