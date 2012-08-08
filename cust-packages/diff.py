def diff_func(set1, set2, lines2, lines1):


  file2_added = set2 - set1
  file2_removed = set1 - set2

  results = []
  results.append('Lines added to')
  count = 1
  for line in lines2:
    if line in file2_added:
      text = str(count) + ': ' + line
      results.append(text)
    count += 1

  results.append('Lines removed from')
  count = 1
  for line in lines1:
    if line in file2_removed:
      text = str(count) + ': ' + line
      results.append(text)
    count += 1
  return results

