#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	IO
%define	pnam	BufferedSelect
Summary:	IO::BufferedSelect - Line-buffered select interface
Name:		perl-IO-BufferedSelect
Version:	1.0
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c6013480c2acf855312c9a184816857
URL:		http://search.cpan.org/dist/IO-BufferedSelect/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The select system call (and the IO::Select interface) allows us to
process multiple streams simultaneously, blocking until one or more of
them is ready for reading or writing. Unfortunately, this requires us
to use sysread and syswrite rather than Perl's buffered I/O functions.
In the case of reading, there are two issues with combining select
with readline: (1) select might block but the data we want is already
in Perl's input buffer, ready to be slurped in by readline; and (2)
select might indicate that data is available, but readline will block
because there isn't a full $/-terminated line available.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/*.pm
%{_mandir}/man3/*
