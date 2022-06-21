floor_long=float(input('Введите длинну пола в метрах: '))
floor_high=float(input('Введите ширину пола в метрах: '))
tile_floor_long=float(input('Введите ширину напольной плитки в метрах: '))
tile_floor_high=float(input('Введите длинну напольной плитки в метрах: '))
tile_wall_side_high =float(input('Введите высоту бортика в метрах: ')) 
tile_wall_long=float(input('Введите ширину насетнной плитки в метрах: '))
tile_wall_high=float(input('Введите длинну настенной плитки в метрах: ')) 
tile_cofficient=float(input('Введите коэфициент расхода плитки: '))
wall_area=4
  
floor_area = round(floor_long*floor_high,2)# Общая площадь пола.
tile_wall_area = round(tile_wall_long*tile_wall_high,2)# Общая площадь одной настенной плитки.
tile_side_area = round(tile_floor_long*tile_wall_side_high*4,2)# Общая площадь бортиков.
tile_floor_area = round(tile_floor_long*tile_floor_high,2)# Общая площадь одной напольной плитки.
tile_wall_count = round((wall_area/tile_wall_area)+(wall_area*tile_cofficient),0)# Расчет количества настенной плитки (общая площадь стен разделить на площадь одной плитки).
tile_floor_count = round((floor_area/tile_floor_area)+(floor_area*tile_cofficient),0)# Расчет количества напольной плитки (общая площадь пола разделиь на площадь одной плитки).
tile_side_count = round((tile_side_area/tile_floor_area)+(tile_side_area*tile_cofficient),0)# Расчет количества напольной плитки бортика (общая площадь бортика разделить на площадь одной плитки).

print('') 
print(f'Общая площадь стен: {wall_area} м2.')
print(f'Общая площадь пола: {floor_area} м2.')
print(f'Площадь настенной плитки: {tile_wall_area} м2.')
print(f'Площадь напольной плитки: {tile_floor_area} м2.')
print('')
print(f'Количество настенной плитки: {int(tile_wall_count)} шт.')
print(f'Количество напольной плитки: {int(tile_floor_count+tile_side_area)} шт.')