from BFSSolution import *

def main():
    """A function demonstrating the use of the GameTreeNode class.
    """ 
    with open('D:\Study Material\Sem V\AI\Lab\8Puzzle\input.txt', 'r') as input_file:
        game_state_as_array = input_file.read().split()
    
    with open('D:\Study Material\Sem V\AI\Lab\8Puzzle\output.txt','a') as output_file:
        solution = BFSSolution(game_state_as_array)
        solution.perform_search_method()
        output_file.write("Algorithm: "+solution.method_name+"\n")
        output_file.write("Heuristic function: "+solution.heuristic_estimate+"\n")
        output_file.write("Elapsed time: "+str(solution.elapsed_time)+" s\n")
        output_file.write("Number of steps required: "+str(solution.count_step())+"\n\n")
        output_file.write(solution.show_path())
        output_file.write("--------------------------------------------------\n\n")


if __name__ == '__main__':
    main()