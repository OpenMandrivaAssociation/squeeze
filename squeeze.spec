%define url_ver %(echo %{version} | cut -c 1-3)

%define major 0
%define apiversion 0.2
%define libname %mklibname %{name} %{apiversion} %{major}
%define develname %mklibname %{name} -d

Summary:	Advanced archive manager for the Xfce
Name:		squeeze
Version:	0.2.3
Release:	12
License:	GPLv2+
Group:		Archiving/Compression
Url:		http://squeeze.xfce.org
Source0:	http://archive.xfce.org/src/apps/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.2.1-TreeView-border.patch
Patch1:		%{name}-0.2.1-recent-documents.patch
BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix

%description
Squeeze is a modern and advanced archive manager for 
the Xfce Desktop Environment.Its design adheres to the 
Xfce philosophy, which basically means Squeeze is both 
fast and easy to use.

%package -n %{libname}
Summary:	Main library for squeeze
Group:		System/Libraries

%description -n %{libname}
Main library for squeeze.

%package -n %{develname}
Summary:	Development files for squeeze
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Development files for squeeze.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
dos2unix TODO

%build
%define Werror_cflags %nil
%configure2_5x \
	--disable-static \
	--enable-gslices \
	--enable-pathbar \
	--enable-toolbar \
	--enable-iter-slices

%make

%install
%makeinstall_std

%find_lang %{name}

desktop-file-install \
    --add-only-show-in="XFCE" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/squeeze
%{_libdir}/thunar-archive-plugin/squeeze.tap
%{_datadir}/applications/squeeze.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/pixmaps/squeeze/*.png

%files -n %{libname}
%{_libdir}/*%{apiversion}.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
