# do not repack jars (works on <= CentOS 5 only)
%{?el5:%define __os_install_post %{nil}}

# do not repack jars
%define __jar_repack %{nil}

Name: topcat
Version: 4.4
Release: 1%{?dist}
Summary: Tool for OPerations on Catalogues And Tables
Group: Sciences/Astronomy
License: GPL
URL: http://www.star.bris.ac.uk/~mbt/topcat/
Source0: ftp://andromeda.star.bris.ac.uk/pub/star/%{name}/v%{version}/%{name}-full.jar
Source1: topcat
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
TOPCAT is an interactive graphical viewer and editor for tabular data. Its aim
is to provide most of the facilities that astronomers need for analysis and
manipulation of source catalogues and other tables, though it can be used for
non-astronomical data as well. It understands a number of different
astronomically important formats (including FITS, VOTable and CDF) and more
formats can be added.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}

%{__install} -p -m 0644 "%{SOURCE0}" "%{buildroot}%{_bindir}/topcat-full.jar"
%{__install} -p -m 0755 "%{SOURCE1}" "%{buildroot}%{_bindir}/topcat"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/topcat-full.jar
%{_bindir}/topcat

%changelog
* Thu Aug 3 2017 Ira W. Snyder <isnyder@lco.global> - 4.4-1
- Update to version 4.4.
* Mon May 2 2016 Ira W. Snyder <isnyder@lco.global> - 4.3.2-1
- Initial build.
