def num_obj(numbers):
  new_list = []
  for num in numbers:
    new_list.append({str(num):chr(num)})
    return new_list

print(num_obj([118,117,120]))
