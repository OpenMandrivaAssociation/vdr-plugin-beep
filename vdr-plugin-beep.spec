
%define plugin	beep
%define name	vdr-plugin-%plugin
%define version	0.0.6
%define rel	17

Summary:	VDR plugin: Notify with a beep
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://deltab.de/vdr/beep.html
Source:		http://deltab.de/vdr/vdr-%plugin-%version.tar.bz2
Patch0:		beep-0.0.6-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This Plugin notify with a beep over the internal mainboard speaker,
to selected VDR events.

%prep
%setup -q -n %plugin-%version
chmod a+x contrib
chmod a+x contrib/Elise.sh
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY contrib


