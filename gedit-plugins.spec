Summary:	gEdit plugins
Summary(pl):	Wtyczki dla gEdit
Name:		gedit-plugins
Version:	2.3.5
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	6925b3f5150a0e265abeb6d4657728d1
URL:		http://gedit.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.3.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	eel-devel >= 2.3.9
BuildRequires:	gedit2-devel >= 2.3.5
BuildRequires:	glib2-devel >= 2.2.3
BuildRequires:	gtksourceview-devel >= 0.6.0
BuildRequires:	intltool >= 0.25
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.3.1
BuildRequires:	libgnomeui-devel >= 2.3.7
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.1-10
Requires:	gedit2 >= 2.3.5
Requires:	libgnomeprintui >= 2.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gEdit plugins.

%description -l pl
Wtyczki dla gEdit.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove obsoleted *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog TODO AUTHORS
%attr(755,root,root) %{_libdir}/gedit-2/plugins/*.so*
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_datadir}/gedit-2/glade/*
