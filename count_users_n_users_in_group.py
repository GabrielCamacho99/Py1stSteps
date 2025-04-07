
def count_users(group):
  count = 0
  for member in get_members(group):
    if not is_group(member):
      count += 1
    else:
      count += count_users(member)
  return count


print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18