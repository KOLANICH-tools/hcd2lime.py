from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-tools/hcd2lime.py , read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

def blobToWriteCommands(b, invalidCallback):
	from .kaitai import parse

	return parsedToWriteCommands(parse(b), invalidCallback)


def parsedToWriteCommands(p, invalidCallback):
	for i, c in enumerate(p.commands):
		if c.opcode.group == c.Group.vendor_specific:
			vSC = c.parameters.payload
			if vSC.command == vSC.Command.write_ram:
				pld = vSC.payload
				yield (pld.address, pld.data)
				continue
			elif vSC.command == vSC.Command.launch_ram:
				yield None

		invalidCallback(i, c)
