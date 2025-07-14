Summary:	CMatrix - show a scrolling 'Matrix' like screen in Linux (curses based)
Summary(pl.UTF-8):	CMatrix - pokazuje efekt spadających znaków znany z filmu "Matrix"
Name:		cmatrix
Version:	1.2a
Release:	8
License:	GPL v2+
Group:		Applications/Terminal
Source0:	http://www.asty.org/cmatrix/dist/%{name}-%{version}.tar.gz
# Source0-md5:	ebfb5733104a258173a9ccf2669968a1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-setfont-consolechars-choice.patch
Patch2:		%{name}-link.patch
URL:		http://www.asty.org/cmatrix/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
Requires(post,postun):	fontpostinst
Requires:	kbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What is CMatrix? :-)

CMatrix is a program I wrote one evening because I didn't want to have
to run Wind*ws to see the cool scrolling lines from 'The Matrix', my
fave movie. If you haven't seen this movie and you are a fan of
computers or sci-fi in general, go see this movie!!!

%description -l pl.UTF-8
What is CMatrix? :-)

CMatrix został napisany w jeden wieczór byś nie musiał uruchamiać M$
Wind*ws, aby zobaczyć na konsoli interesujący efekt spadających znaków
znany z filmu "Matrix". Jeżeli nie widziałeś tego filmu, a jesteś
fanem komputerów i sci-fi w ogólności - biegnij zobaczyć ten film!!!

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--with-setfont
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/fonts/misc,%{_bindir}} \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT/lib/kbd/consolefonts

install cmatrix $RPM_BUILD_ROOT%{_bindir}
install cmatrix.1 $RPM_BUILD_ROOT%{_mandir}/man1
install mtx.pcf $RPM_BUILD_ROOT%{_datadir}/fonts/misc
install matrix.psf.gz $RPM_BUILD_ROOT/lib/kbd/consolefonts

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/fonts/misc/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fonts/misc/*
/lib/kbd/consolefonts/*
%{_mandir}/man1/*
