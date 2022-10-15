srpm:
	dnf -y install /usr/bin/spectool
	spectool --get '$(spec)' --directory '$(dir $(spec))'
	cd '$(dir $(spec))' && sha512sum -c sources
	rpmbuild -bs --define '_sourcedir $(dir $(spec))' --define '_srcrpmdir $(outdir)' '$(spec)'
