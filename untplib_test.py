import untplib
  try:
    i = i + 1
    if i == 300:
      print('sync ntp time server...')
      resp=c.request('pool.ntp.org', version=3, port=123)
      i = 0
  except untplib.NTPException as e:
    print (e)