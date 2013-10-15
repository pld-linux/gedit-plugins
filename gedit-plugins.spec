Summary:	gedit plugins
Summary(pl.UTF-8):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	3.10.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-plugins/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	dde9831b855abdd53dfd31c12be10ea5
URL:		http://www.gnome.org/projects/gedit/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gedit-devel >= 3.8.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtksourceview3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgit2-glib-devel >= 0.0.2
BuildRequires:	libpeas-devel >= 1.8.0
BuildRequires:	libpeas-gtk-devel >= 1.8.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-dbus-devel >= 0.82
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	gedit >= 3.8.0
Requires:	gtk+3 >= 3.4.0
Requires:	gtksourceview3 >= 3.0.0
Requires:	gucharmap-libs >= 3.0.0
Requires:	libpeas-gtk >= 1.8.0
Requires:	libpeas-loader-python3 >= 1.8.0
Requires:	python-dbus >= 0.82
Requires:	python-pycairo
Requires:	python-pygobject3 >= 3.0.0
Requires:	vte >= 0.34.0
Requires:	zeitgeist-libs >= 0.9.12
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for gedit.

%description -l pl.UTF-8
Zestaw wtyczek dla gedita.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-python \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove not needed files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gedit/plugins/*.la

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/gedit/plugins/libbookmarks.so
%{_libdir}/gedit/plugins/bookmarks.plugin

%{_libdir}/gedit/plugins/bracketcompletion.plugin
%{_libdir}/gedit/plugins/bracketcompletion.py*

%{_libdir}/gedit/plugins/charmap.plugin
%dir %{_libdir}/gedit/plugins/charmap
%{_libdir}/gedit/plugins/charmap/*.py*

%{_libdir}/gedit/plugins/codecomment.plugin
%{_libdir}/gedit/plugins/codecomment.py*

%{_libdir}/gedit/plugins/colorpicker.plugin
%{_libdir}/gedit/plugins/colorpicker.py*

%{_libdir}/gedit/plugins/colorschemer.plugin
%dir %{_libdir}/gedit/plugins/colorschemer
%{_libdir}/gedit/plugins/colorschemer/*.py*
%{_datadir}/gedit/plugins/colorschemer

%{_libdir}/gedit/plugins/commander.plugin
%dir %{_libdir}/gedit/plugins/commander
%dir %{_libdir}/gedit/plugins/commander/commands
%{_libdir}/gedit/plugins/commander/*.py*
%{_libdir}/gedit/plugins/commander/commands/*.py*
%{_datadir}/gedit/plugins/commander

%{_libdir}/gedit/plugins/dashboard.plugin
%dir %{_libdir}/gedit/plugins/dashboard
%{_libdir}/gedit/plugins/dashboard/*.py*

%attr(755,root,root) %{_libdir}/gedit/plugins/libdrawspaces.so
%{_libdir}/gedit/plugins/drawspaces.plugin

%{_libdir}/gedit/plugins/git.plugin
%dir %{_libdir}/gedit/plugins/git
%{_libdir}/gedit/plugins/git/*.py*

%{_libdir}/gedit/plugins/gpdefs.py*

%{_libdir}/gedit/plugins/joinlines.plugin
%{_libdir}/gedit/plugins/joinlines.py*

%{_libdir}/gedit/plugins/multiedit.plugin
%dir %{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit/*.py*

%{_libdir}/gedit/plugins/smartspaces.plugin
%{_libdir}/gedit/plugins/smartspaces.py*

%{_libdir}/gedit/plugins/synctex.plugin
%dir %{_libdir}/gedit/plugins/synctex
%{_libdir}/gedit/plugins/synctex/*.py*

%{_libdir}/gedit/plugins/terminal.plugin
%{_libdir}/gedit/plugins/terminal.py*

%{_libdir}/gedit/plugins/textsize.plugin
%dir %{_libdir}/gedit/plugins/textsize
%{_libdir}/gedit/plugins/textsize/*.py*

%{_libdir}/gedit/plugins/wordcompletion.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libwordcompletion.so

%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
