%define	pkgname gnuplot
%define name	octave-%{pkgname}
%define version 1.0.1
%define release %mkrel 1

Summary:	Gnuplot scripts for Octave
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/gnuplot/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7
Requires:	gnuplot >= 4.0
BuildRequires:	octave-devel >= 2.9.7, MesaGL-devel, MesaGLU-devel
BuildRequires:	gnuplot >= 4.0
BuildArch:	noarch

%description
This package provides scripts that can save data in gnuplot-readable
formats, specify the gnuplot commands used to produce
graphics, and invoke gnuplot. 

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
rm -rf %{buildroot}
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"
mv %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/Changelog .
rm -f %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/COPYRIGHT
rm -f %{buildroot}%{_datadir}/octave/packages/%{pkgname}-%{version}/LICENSE.txt

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean
%__rm -rf %{buildroot}

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION Changelog
%{_datadir}/octave/packages/%{pkgname}-%{version}
