%define plugin	beep

Summary:	VDR plugin: Notify with a beep
Name:		vdr-plugin-%plugin
Version:	0.1.2
Release:	5
Group:		Video
License:	GPL
URL:		http://www.deltab.de/content/view/25/62
Source:		vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This Plugin notify with a beep over the internal mainboard speaker,
to selected VDR events.

%prep
%setup -q -n %plugin-%version
chmod a+x contrib
chmod a+x contrib/Elise.sh
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY contrib




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2010.0
+ Revision: 396080
- new version

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.1-2mdv2009.1
+ Revision: 359288
- rebuild for new vdr

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 0.1.1-1mdv2009.0
+ Revision: 205452
- new version
- drop i18n patch, fixed upstream
- update URL

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-17mdv2009.0
+ Revision: 197903
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-16mdv2009.0
+ Revision: 197634
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-15mdv2008.1
+ Revision: 145040
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6-14mdv2008.1
+ Revision: 144988
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-13mdv2008.1
+ Revision: 103066
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-12mdv2008.0
+ Revision: 49972
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-11mdv2008.0
+ Revision: 42059
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6-10mdv2008.0
+ Revision: 22711
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-9mdv2007.0
+ Revision: 90894
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-8mdv2007.1
+ Revision: 73958
- rebuild for new vdr
- Import vdr-plugin-beep

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2007.0
- rebuild for new vdr

* Sun Jun 04 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2007.0
- initial Mandriva release

