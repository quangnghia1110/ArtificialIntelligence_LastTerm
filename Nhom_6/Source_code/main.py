import Kakuro_Problem as kakuro
import backtracking_search_with_MAC_solver as kakuro_solver

if __name__ == '__main__':
    rows=12
    columns=10
    Horizontal = [['#','#','#','#','#','#','#','#','#','#'],
                ['#', 18, 0, 0, 0, 0, 0, 12, 0, 0],
                [39, 0, 0, 0, 0, 0, 0, 10, 0, 0],
                [12, 0, 0, 0, '#', 11, 0, 0, 0, 0],
                ['#', 9, 0, 0, 12, 0, 0, 0, '#', '#'],
                ['#', 17, 0, 0, 0, 0, '#', 8, 0, 0],
                [14, 0, 0, 6, 0, 0, 0, 11 , 0, 0],
                [9, 0, 0, '#', 14, 0, 0, 0, 0, '#'],
                ['#', '#', 9, 0, 0, 0, 8, 0, 0, '#'],
                [11, 0, 0, 0, 0, '#', 11, 0, 0, 0],
                [17, 0, 0, 37 ,0 ,0 ,0 ,0 ,0 ,0],
                [9, 0, 0, 20, 0, 0, 0, 0, 0, '#']]

    Vertical = [['#','#',31,32,12,10,21,'#',6,19],
                ['#',5,0,0,0,0,0,'#',0,0],
                ['#',0,0,0,0,0,0,13,0,0],
                ['#',0,0,0,'#',15,0,0,0,0],
                ['#','#',0,0,4,0,0,0,29,5],
                ['#',7,0,0,0,0,10,'#',0,0],
                ['#',0,0,'#',0,0,0,32,0,0],
                ['#',0,0,6,12,0,0,0,0,'#'],
                ['#',20,11,0,0,0,'#',0,0,10],
                ['#',0,0,0,0,4,10,0,0,0],
                ['#',0,0,'#',0,0,0,0,0,0],
                ['#',0,0,'#',0,0,0,0,0,'#']]
    
    kakuro_game = kakuro.Kakuro_Problem(rows, columns, Horizontal, Vertical)
    kakuro_game.show_img((10, 10))

    solver = kakuro_solver.backtracking_search_with_MAC_solver()
    solver.train(kakuro_game)
    assignment = solver.solve()
   
    kakuro_game.show(assignment)
    kakuro_game.fill_in_value_cells(assignment)
    kakuro_game.show_img((10, 10))