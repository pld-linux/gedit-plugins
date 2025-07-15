Summary:	gedit plugins
Summary(pl.UTF-8):	Wtyczki dla gedita
Name:		gedit-plugins
Version:	48.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	https://download.gnome.org/sources/gedit-plugins/48/%{name}-%{version}.tar.xz
# Source0-md5:	527d365b89ca4848732c8c3298b1fe94
URL:		https://wiki.gnome.org/Apps/Gedit
BuildRequires:	appstream-glib
BuildRequires:	gedit-devel >= 48.1
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.64
BuildRequires:	libgedit-gtksourceview-devel >= 299
BuildRequires:	libpeas-devel >= 1.14.1
BuildRequires:	libpeas-gtk-devel >= 1.14.1
BuildRequires:	meson >= 0.57
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-build >= 4.1-10
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.28.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	gedit >= 48.1
Requires:	glib2 >= 1:2.64
# Gtk-3.0 typelib
Requires:	gtk+3 >= 3.22
# Gucharmap-2.90 typelib
Requires:	gucharmap-libs >= 3.0.0
# GtkSource-300 typelib
Requires:	libgedit-gtksourceview >= 299
# Peas-1.0, PeasGtk-1.0 typelibs
Requires:	libpeas-gtk >= 1.14.1
Requires:	libpeas-loader-python3 >= 1.14.1
Requires:	python3-dbus >= 0.82
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.0.0
# Vte-2.91 typelib
Requires:	vte >= 0.38.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of plugins for gedit.

%description -l pl.UTF-8
Zestaw wtyczek dla gedita.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{_libdir}/gedit/plugins
%py3_ocomp $RPM_BUILD_ROOT%{_libdir}/gedit/plugins

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
# common
%dir %{_libdir}/gedit/plugins/__pycache__
%{_libdir}/gedit/plugins/gpdefs.py
%{_libdir}/gedit/plugins/__pycache__/gpdefs.cpython-*.py[co]

# plugins below

%{_libdir}/gedit/plugins/bookmarks.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libbookmarks.so
%{_datadir}/metainfo/gedit-bookmarks.metainfo.xml

%{_libdir}/gedit/plugins/bracketcompletion.plugin
%{_libdir}/gedit/plugins/bracketcompletion.py
%{_libdir}/gedit/plugins/__pycache__/bracketcompletion.cpython-*.py[co]
%{_datadir}/metainfo/gedit-bracketcompletion.metainfo.xml

%{_libdir}/gedit/plugins/charmap.plugin
%dir %{_libdir}/gedit/plugins/charmap
%{_libdir}/gedit/plugins/charmap/*.py
%{_libdir}/gedit/plugins/charmap/__pycache__
%{_datadir}/metainfo/gedit-charmap.metainfo.xml

%{_libdir}/gedit/plugins/codecomment.plugin
%{_libdir}/gedit/plugins/codecomment.py
%{_libdir}/gedit/plugins/__pycache__/codecomment.cpython-*.py[co]
%{_datadir}/metainfo/gedit-codecomment.metainfo.xml

%{_libdir}/gedit/plugins/colorpicker.plugin
%{_libdir}/gedit/plugins/colorpicker.py
%{_libdir}/gedit/plugins/__pycache__/colorpicker.cpython-*.py[co]
%{_datadir}/metainfo/gedit-colorpicker.metainfo.xml

%{_libdir}/gedit/plugins/drawspaces.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libdrawspaces.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_datadir}/metainfo/gedit-drawspaces.metainfo.xml

%{_libdir}/gedit/plugins/joinlines.plugin
%{_libdir}/gedit/plugins/joinlines.py
%{_libdir}/gedit/plugins/__pycache__/joinlines.cpython-*.py[co]
%{_datadir}/metainfo/gedit-joinlines.metainfo.xml

%{_libdir}/gedit/plugins/multiedit.plugin
%dir %{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit/*.py
%{_libdir}/gedit/plugins/multiedit/__pycache__
%{_datadir}/metainfo/gedit-multiedit.metainfo.xml

%{_libdir}/gedit/plugins/sessionsaver.plugin
%dir %{_libdir}/gedit/plugins/sessionsaver
%{_libdir}/gedit/plugins/sessionsaver/*.py
%{_libdir}/gedit/plugins/sessionsaver/__pycache__
%dir %{_libdir}/gedit/plugins/sessionsaver/store
%{_libdir}/gedit/plugins/sessionsaver/store/*.py
%{_libdir}/gedit/plugins/sessionsaver/store/__pycache__
%{_datadir}/gedit/plugins/sessionsaver

%attr(755,root,root) %{_libdir}/gedit/plugins/libsmartspaces.so
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_datadir}/metainfo/gedit-smartspaces.metainfo.xml

%{_libdir}/gedit/plugins/terminal.plugin
%{_libdir}/gedit/plugins/terminal.py
%{_libdir}/gedit/plugins/__pycache__/terminal.cpython-*.py[co]
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_datadir}/metainfo/gedit-terminal.metainfo.xml

%{_libdir}/gedit/plugins/wordcompletion.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/libwordcompletion.so
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_datadir}/metainfo/gedit-wordcompletion.metainfo.xml
