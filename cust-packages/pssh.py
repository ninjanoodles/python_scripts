import pexpect 

def ssh_func(hostname, user, password, command):

  prompt="\#"
  child = pexpect.spawn ("ssh %s" %(hostname))
  child.expect("assword: ",timeout=120)
  child.sendline(password)
  child.expect(prompt)
  child.sendline(command)
  child.expect(prompt)
  response = child.before
  child.close()
  lines=response.split('\r\n')
  del  lines[0]
  del  lines[-1]
  return lines
