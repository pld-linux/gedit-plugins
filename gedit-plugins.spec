Summary:	gedit plugins
Summary(pl.UTF-8):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	3.16.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-plugins/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	1ba8fcb8535833dfdd3176cba24eb37e
URL:		http://www.gnome.org/projects/gedit/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gedit-devel >= 3.16.0
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.9.0
BuildRequires:	gtksourceview3-devel >= 3.14.0
# Gucharmap-2.90 typelib
BuildRequires:	gucharmap-libs >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgit2-glib-devel >= 0.0.6
BuildRequires:	libpeas-devel >= 1.8.0
BuildRequires:	libpeas-gtk-devel >= 1.8.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python-dbus-devel >= 0.82
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRequires:	tar >= 1:1.22
# Vte-2.91 typelib
BuildRequires:	vte >= 0.38
BuildRequires:	xz
BuildRequires:	yelp-tools
# pkgconfig(zeitgeist-2.0) + Zeitgeist-2.0 typelib
BuildRequires:	zeitgeist-devel >= 0.9.12
Requires:	gedit >= 3.16.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.9.0
Requires:	gtksourceview3 >= 3.14.0
# Gucharmap-2.90 typelib
Requires:	gucharmap-libs >= 3.0.0
Requires:	libgit2-glib >= 0.0.6
Requires:	libpeas-gtk >= 1.8.0
Requires:	libpeas-loader-python3 >= 1.8.0
Requires:	python3-dbus >= 0.82
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.0.0
# Vte-2.91 typelib
Requires:	vte >= 0.38.0
# libzeitgeist-2.0 so + Zeitgeist-2.0 typelib
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
%doc AUTHORS ChangeLog NEWS README
# common
%dir %{_libdir}/gedit/plugins/__pycache__
%{_libdir}/gedit/plugins/gpdefs.py
%{_libdir}/gedit/plugins/__pycache__/gpdefs.cpython-*.py[co]

# plugins below

%{_libdir}/gedit/plugins/bookmarks.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libbookmarks.so
%{_datadir}/appdata/gedit-bookmarks.metainfo.xml

%{_libdir}/gedit/plugins/bracketcompletion.plugin
%{_libdir}/gedit/plugins/bracketcompletion.py
%{_libdir}/gedit/plugins/__pycache__/bracketcompletion.cpython-*.py[co]
%{_datadir}/appdata/gedit-bracketcompletion.metainfo.xml

%{_libdir}/gedit/plugins/charmap.plugin
%dir %{_libdir}/gedit/plugins/charmap
%{_libdir}/gedit/plugins/charmap/*.py
%{_libdir}/gedit/plugins/charmap/__pycache__
%{_datadir}/appdata/gedit-charmap.metainfo.xml

%{_libdir}/gedit/plugins/codecomment.plugin
%{_libdir}/gedit/plugins/codecomment.py
%{_libdir}/gedit/plugins/__pycache__/codecomment.cpython-*.py[co]
%{_datadir}/appdata/gedit-codecomment.metainfo.xml

%{_libdir}/gedit/plugins/colorpicker.plugin
%{_libdir}/gedit/plugins/colorpicker.py
%{_libdir}/gedit/plugins/__pycache__/colorpicker.cpython-*.py[co]
%{_datadir}/appdata/gedit-colorpicker.metainfo.xml

%{_libdir}/gedit/plugins/colorschemer.plugin
%dir %{_libdir}/gedit/plugins/colorschemer
%{_libdir}/gedit/plugins/colorschemer/*.py
%{_libdir}/gedit/plugins/colorschemer/__pycache__
%{_datadir}/gedit/plugins/colorschemer
%{_datadir}/appdata/gedit-colorschemer.metainfo.xml

%{_libdir}/gedit/plugins/commander.plugin
%dir %{_libdir}/gedit/plugins/commander
%dir %{_libdir}/gedit/plugins/commander/commands
%{_libdir}/gedit/plugins/commander/*.py
%{_libdir}/gedit/plugins/commander/__pycache__
%{_libdir}/gedit/plugins/commander/commands/*.py*
%{_libdir}/gedit/plugins/commander/commands/__pycache__
%{_datadir}/gedit/plugins/commander
%{_datadir}/appdata/gedit-commander.metainfo.xml

%{_libdir}/gedit/plugins/dashboard.plugin
%dir %{_libdir}/gedit/plugins/dashboard
%{_libdir}/gedit/plugins/dashboard/*.py
%{_libdir}/gedit/plugins/dashboard/__pycache__
%{_datadir}/appdata/gedit-dashboard.metainfo.xml

%{_libdir}/gedit/plugins/drawspaces.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libdrawspaces.so
%{_datadir}/appdata/gedit-drawspaces.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml

%{_libdir}/gedit/plugins/git.plugin
%dir %{_libdir}/gedit/plugins/git
%{_libdir}/gedit/plugins/git/*.py*
%{_libdir}/gedit/plugins/git/__pycache__
%{_datadir}/appdata/gedit-git.metainfo.xml

%{_libdir}/gedit/plugins/joinlines.plugin
%{_libdir}/gedit/plugins/joinlines.py
%{_libdir}/gedit/plugins/__pycache__/joinlines.cpython-*.py[co]
%{_datadir}/appdata/gedit-joinlines.metainfo.xml

%{_libdir}/gedit/plugins/multiedit.plugin
%dir %{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit/*.py
%{_libdir}/gedit/plugins/multiedit/__pycache__
%{_datadir}/appdata/gedit-multiedit.metainfo.xml

%{_libdir}/gedit/plugins/smartspaces.plugin
%{_libdir}/gedit/plugins/smartspaces.py
%{_libdir}/gedit/plugins/__pycache__/smartspaces.cpython-*.py[co]
%{_datadir}/appdata/gedit-smartspaces.metainfo.xml

%{_libdir}/gedit/plugins/synctex.plugin
%dir %{_libdir}/gedit/plugins/synctex
%{_libdir}/gedit/plugins/synctex/*.py
%{_libdir}/gedit/plugins/synctex/__pycache__
%{_datadir}/appdata/gedit-synctex.metainfo.xml

%{_libdir}/gedit/plugins/terminal.plugin
%{_libdir}/gedit/plugins/terminal.py
%{_libdir}/gedit/plugins/__pycache__/terminal.cpython-*.py[co]
%{_datadir}/appdata/gedit-terminal.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml

%{_libdir}/gedit/plugins/textsize.plugin
%dir %{_libdir}/gedit/plugins/textsize
%{_libdir}/gedit/plugins/textsize/*.py
%{_libdir}/gedit/plugins/textsize/__pycache__
%{_datadir}/appdata/gedit-textsize.metainfo.xml

%{_libdir}/gedit/plugins/wordcompletion.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libwordcompletion.so
%{_datadir}/appdata/gedit-wordcompletion.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml

%{_libdir}/gedit/plugins/zeitgeist.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libzeitgeist.so
%{_datadir}/appdata/gedit-zeitgeist.metainfo.xml
