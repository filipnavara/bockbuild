class PixmanPackage (CairoGraphicsPackage):
	def __init__ (self):
		CairoGraphicsPackage.__init__ (self, 'pixman', '0.30.0')
		
		#This package would like to be built with fat binaries
		if Package.profile.m64 == True:
			self.fat_build = True

	def arch_build (self, arch):
		if arch == 'darwin-fat': #multi-arch  build pass
			self.local_ld_flags = ['-arch i386' , '-arch x86_64']
			self.local_gcc_flags = ['-arch i386' , '-arch x86_64', '-Os']
			self.local_configure_flags = ['--disable-dependency-tracking']

		Package.arch_build (self, arch)

PixmanPackage ()
