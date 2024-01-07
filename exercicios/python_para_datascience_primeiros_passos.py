"""1) Faça um programa que tenha a seguinte lista contendo os 
valores de gastos de uma empresa de papel [2172.54, 3701.35, 
3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 
3219.08]. Com esses valores, faça um programa que calcule a 
média de gastos. Dica: use as funções built-in sum() e len()."""

total_gasto = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 
               2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
# ele quer a média (preciso do somatório e da quantidade de valores)
somatorio = sum(total_gasto)
qntd_total = len(total_gasto)
media = somatorio / qntd_total
print(media)