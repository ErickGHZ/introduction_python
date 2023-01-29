"""
Soccer Team

You need to calculate the points earned by a soccer team. 
The team won 18 games and ended 7 games as a draw.  
A win brings 3 points, while a draw brings 1.
"""
puntos_por_ganar=3
puntos_por_empatar=1
juegos_gananados = 18
juegos_empatados = 7
puntos_ganados_por_ganar = juegos_gananados * puntos_por_ganar
puntos_ganados_por_empatar = juegos_empatados * puntos_por_empatar
print("Los puntos totales ganados del team son:",puntos_ganados_por_ganar + puntos_ganados_por_empatar)