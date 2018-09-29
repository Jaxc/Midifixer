#!/usr/bin/python3

import os

statinfo = os.stat('Disney_Themes_-_DuckTales.mid')
print (statinfo)

midi_input = open("Disney_Themes_-_DuckTales.mid", 'rb', 1)
midi_input.seek(0, os.SEEK_END)
size = midi_input.tell()
midi_input.seek(0)

# Check header chunk id
header_ascii = midi_input.read(4)
if header_ascii != b'MThd':
	print(header_ascii)
	print("Not a Midi file")
	quit()

# Get header chunk length
header_len = int.from_bytes(midi_input.read(4), byteorder='big')

# Get header chunk format
# 0 = single track file format
# 1 = multiple track file format
# 2 = multiple song format, not supported
header_format = int.from_bytes(midi_input.read(2), byteorder='big')
if header_format != 0 and header_format != 1:
	print ("Unsupported header format: ", header_format)

header_n_chunks = int.from_bytes(midi_input.read(2), byteorder='big')

header_time_division = int.from_bytes(midi_input.read(2), byteorder='big')

for chunk in range(0, header_n_chunks):
	chunk_header_ascii = midi_input.read(4)
	if chunk_header_ascii != b'MTrk':
		print(midi_input.tell())
		print(header_ascii)
		print("Incorrect chunk header")
		quit()
	header_len = int.from_bytes(midi_input.read(4), byteorder='big')

	while header_len :
		delta_t = int.from_bytes(midi_input.read(1), byteorder='big')
		print (delta_t)

		event_type = int.from_bytes( midi_input.read(1) , byteorder='big')

		event_high, event_low = event_type >> 4, event_type & 0x0F

		print(event_high, event_low)
		print (header_len)
		if event_type == 0xFF:
			meta_event_type = int.from_bytes(midi_input.read(1), byteorder='big')
			meta_event_len = int.from_bytes(midi_input.read(1), byteorder='big')
			meta_event_data = midi_input.read(meta_event_len)
			if meta_event_type == 0x00 :
				print("0x00")
			elif meta_event_type == 0x01 :
				print("0x01")
			elif meta_event_type == 0x02 :
				print("0x02")
			elif meta_event_type == 0x03 :
				print(meta_event_data)
			elif meta_event_type == 0x04 :
				print("0x04")
			elif meta_event_type == 0x05 :
				print("0x05")
			elif meta_event_type == 0x06 :
				print("0x06")
			elif meta_event_type == 0x07 :
				print("0x07")
			elif meta_event_type == 0x20 :
				print("0x20")
			elif meta_event_type == 0x2F :
				print("0x2F")
			elif meta_event_type == 0x51 :
				print("0x51")
			elif meta_event_type == 0x54 :
				print("0x54")
			elif meta_event_type == 0x58 :
				print("0x58")
			elif meta_event_type == 0x59 :
				print("0x59")
			elif meta_event_type == 0x7F :
				print("0x7F")
			else :
				print("Unsupported")
				quit()

			header_len = header_len - meta_event_len - 4
		

		elif event_high == 0x08:
			print("Note off")
			midi_input.read(2)
			header_len = header_len - 3

		elif event_high == 0x09:
			print("Note on")
			midi_input.read(2)
			header_len = header_len - 3

		elif event_high == 0x0A:
			print("Polyphonic pressure")
			midi_input.read(2)
			header_len = header_len - 3

		elif event_high == 0x0B:
			print("Control Change")
			midi_input.read(2)
			header_len = header_len - 3

		elif event_high == 0x0C:
			print("Program chańge")
			midi_input.read(1)
			header_len = header_len - 2

		elif event_high == 0x0D:
			print("Channel pressure")
			midi_input.read(1)
			header_len = header_len - 2

		elif event_high == 0x0E:
			print("Pitchbbend")
			midi_input.read(2)
			header_len = header_len - 3

		elif event_high == 0x02:
			print("Unknown event")
			midi_input.read(1)
			header_len = header_len - 2

		elif event_high == 0x00:
			print("Unknown event")
			midi_input.read(1)
			header_len = header_len - 2

		else :
			print ("Incorrect Midi command, exiting")
			exit()
	#while byte:
#	byte = midi_input.read(1)
	#if not byte:
	#	break
#	print ("{}".format(byte))
