import uos

logo = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00<\x01\x03\x00\x00\x00\x94\xf8 \x86\x00\x00\x00\x06PLTE\xff\xff\xff\x00\x00\x00U\xc2\xd3~\x00\x00\x00\tpHYs\x00\x00\x0e\xc4\x00\x00\x0e\xc4\x01\x95+\x0e\x1b\x00\x00\x01\xdfIDAT(\x91\xb5\xd2\xb1n\xdb0\x10\x06\xe0\x9f\x95k\xb2\x80[\xc9\xedP\x01U-\xf5\r\xec\xcd\x83\x11\xa9\xe8\x8b\xf8\x11\xe2-\x9b\xe81@\x83\xbe\x81\xf2*22\xb4\x05\x8a\xce\x1d\xe5d(\xba)[\x06A\xd7;J\xb2\x82"k\t\x88"?\x1c\x8f\xd4Q\xd0\xa5\xae\x90S\x83\x18y\rn&\xd1K\x9cc\x8a\xa4<\x0f\x05\x96\x01\xfc\x06S\x0f\xd9\x16_\x88\x80m\x04hja\xb3PYh \x8b$n\xca\xe0\x93\x95a\x86\xae\xd9\x0c\xaa\x94\xc1\xc7J_\xd3=Qq8\x12\xc5T\x8fp\xd3\xc3\x87\x01>\x1d:\x98\x0f\xa0\xf7\x1d\xbc\xa8t\x81]\x85\xc2\xdf\x97\x88\xc0@\xc4\x11\x15\xaeI\xf5\x11\x03\xb4=\xfc\xe9`u\x82\xef\x1d\xe4\xf1\x00\x97\x1d\x9c\xc5\x9c\xa3\x8d\xa9\xc2e\xbf\xcb\xc2\xe7\x93G\xfeg\x07F@\xcb\xb6\xfa\x07\xaenu\x11\xee\x88\x16\x9aO\x1ay?q\xf5[\x17k\x01\xef(p\xc4\x9e#\xb6\x02J@\x1dao\xf5"\xdb\xc9\xf8\xdeu\xc8&pO\xdf\x14\x12\x9e\x94Z\xaa\xeb\x13\xd9\xb4E\xfc\xa0\xf6v\xca%\xc4+\x0eu\x05U\xad\xf4$\x05M-\xc6\xc5%\xfegS5\xdc\x06j\xd8r\x1a\xc2\xdd\xb2G=\xcc&(9\xc4S\xd6vW\x1f\xf2?\x91\x92|\x0c\xcf*\x86\xc0s\x8b=\xe6\xb6\x83w8P\x13\xd3\r5+,\x056\xea\x8e\xda\x94\xbeRsa\xc3\x13\xe4\x0e2#I\x1fA"`\x1e-\t\x05&\x0cv\x81Z[\\D\x02\xcfRb0\xb5\xe6\x88\x99\xc0\xdcA\xe4\x00\x02\xab\xa7!\x19a\xee\x92&.\xe9\xd3\xf0\xe6_x\xbby\xc9\x07[J\x8e\x9c\xbe9x\xcf\x10\x8e\xf0\xdaE\x98\x11\x82\xcd\xf3;jz\xf8%\xe02\x99\xae\xc0\x81\x1b\x06H\x1f\x0c4\x97/\x97\x12j\xaa\xcbrm\xd6\x86\xab\xb5\xedo\x82&\x08\xce\x02\xdd\xccN\xb7\xe7S\xad*x\xed\tf\xe3\xeb/O\x13NGB\xcf\x87.\x00\x00\x00\x00IEND\xaeB`\x82' 

try:
	uos.mkdir('/media')
except:
	pass

media = uos.listdir('/media')

if not "hackerhotel.png" in media:
	try:
		f = open("/media/hackerhotel.png", 'wb')
		f.write(logo)
		f.close()
		print("Logo installed.")
	except:
		print("Could not install logo.")