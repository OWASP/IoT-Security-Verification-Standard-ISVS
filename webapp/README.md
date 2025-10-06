# ISVS Interactive Tool

🚀 **Live Demo**: [https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/](https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/)

An interactive web application for the OWASP IoT Security Verification Standard (ISVS). Track your IoT security verification progress with an easy-to-use checklist interface.

---

## ✨ Features

- ✅ **Interactive Checklist** - Mark requirements as completed with one click
- 🔍 **Smart Filtering** - Filter by security level (L1/L2/L3) and category (V1-V5)
- 📊 **Progress Tracking** - Visual dashboards showing real-time completion status
- 💾 **Auto-Save** - Progress automatically saved to browser localStorage
- 📄 **Export Reports** - Generate CSV/JSON compliance reports
- 🔗 **Deep Linking** - Share specific requirements via URL
- 📱 **Mobile-Friendly** - Responsive design for on-site testing
- 🌙 **Dark Mode** - Easy on the eyes for extended use
- ♿ **Accessible** - WCAG 2.1 Level AA compliant

---

## 🎯 Quick Start

### For End Users

1. **Open the tool**: [Launch ISVS Tool](https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/)
2. **Filter requirements**: Select your device's security level (L1, L2, or L3)
3. **Start verification**: Check off requirements as you verify them
4. **Export report**: Download your compliance report as CSV or JSON

**No installation required** - works directly in your browser!

### For Developers

See [DEVELOPMENT.md](./DEVELOPMENT.md) for setup instructions.

---

## 📖 How to Use

### For Security Auditors

1. **Filter to security level**: Select L1, L2, or L3 based on the device risk profile
2. **Track verification**: Check requirements as you verify them during testing
3. **Add evidence notes**: Document test cases or evidence (e.g., "Verified in TC-AUTH-001")
4. **Export audit report**: Download CSV to attach to your audit documentation

**Example Workflow**:
```
Smart Camera Audit (L2 Device)
→ Filter: L2 only (98 requirements)
→ Check V2.1.1: "Verified unique device ID per camera"
→ Check V2.1.3: "Tested authentication - see TC-AUTH-001"
→ Export CSV: "ISVS_SmartCamera_Audit_2025-10-05.csv"
```

### For IoT Developers

1. **Filter by product level**: Select requirements applicable to your device
2. **Sprint planning**: Export filtered requirements as CSV to import into Jira/GitHub
3. **Track implementation**: Check off requirements as you implement security controls
4. **Share with team**: Copy deep links to specific requirements

**Example Workflow**:
```
Fitness Tracker Development (L1 Device)
→ Filter: L1 only (67 requirements)
→ Export CSV
→ Import to Jira as subtasks
→ Mark "V2.1.1" complete when implemented
```

### For Compliance Managers

1. **View progress dashboard**: Real-time completion percentage across all categories
2. **Generate reports**: Export compliance certificates for stakeholder meetings
3. **Share status**: Send deep links to team members for specific requirements
4. **Track over time**: Export JSON snapshots for historical comparison

**Example Workflow**:
```
Quarterly Compliance Review
→ View overall: 85/165 (51%) complete
→ Drill down: V4 Communications 91% complete
→ Export PDF compliance certificate
→ Present to executive team
```

---

## 🔧 Technical Details

### Architecture

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite 5
- **Styling**: Tailwind CSS 3
- **State Management**: Zustand (with localStorage persistence)
- **Routing**: React Router 6
- **Data Source**: Auto-generated JSON from ISVS markdown files

### Bundle Size

- **Total Bundle**: ~120 KB uncompressed (~40 KB gzipped)
- **ISVS Data**: ~30 KB (165 requirements)
- **Runtime Code**: ~90 KB (React + dependencies)

### Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Mobile**: iOS Safari 14+, Chrome Android 90+

### Performance

- First Contentful Paint: <1.5s
- Time to Interactive: <3s
- Lighthouse Score: 95+

---

## 📋 Data Privacy & Security

### Local-Only Storage

**All data is stored locally in your browser** (localStorage). Nothing is sent to any server.

- ✅ Your verification progress is private
- ✅ Notes and annotations never leave your device
- ✅ No cookies, no tracking, no analytics
- ✅ Works completely offline after initial load

### Data Backup

Export your state as JSON to backup your progress:

1. Click "Export" → "Export JSON"
2. Save file: `ISVS_State_2025-10-05.json`
3. Import on another device: "Import State" button

### Clearing Data

To reset all progress:

1. Click "Settings" → "Reset Progress"
2. Or clear browser data for `owasp.org`

**Warning**: This cannot be undone unless you've exported your state.

---

## 🚀 Deployment

### Hosting

- **Platform**: GitHub Pages (free)
- **URL**: [https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/](https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/)
- **Cost**: $0/month
- **Uptime**: 99.9% (GitHub SLA)

### CI/CD Workflow

Automatic deployment on push to `main` or `isvs-tool` branches:

1. **Data Generation**: `tools/export.py` generates `isvs-data.json` from markdown
2. **Build**: Vite builds optimized production bundle
3. **Deploy**: Artifacts deployed to GitHub Pages `/isvs-tool/` path

See [`.github/workflows/deploy-tool.yml`](../.github/workflows/deploy-tool.yml)

---

## 📊 Export Formats

### CSV Export

**Use Case**: Import to Excel, Jira, or compliance tools

**Columns**:
- Requirement ID
- Category
- Description
- Level 1/2/3 (✓/✗)
- Status (Completed/Pending)
- Notes
- Completed Date

**Example**:
```csv
Requirement ID,Category,Description,L1,L2,L3,Status,Notes
V1.1.1,V1: IoT Ecosystem,"Verify that the IoT system is developed...",✓,✓,✓,Completed,"Design review 10/5"
```

### JSON Export

**Use Case**: Backup state, share with team, import to another browser

**Structure**:
```json
{
  "version": "1.0",
  "exportDate": "2025-10-05T14:30:00Z",
  "totalRequirements": 165,
  "completedCount": 85,
  "checkedItems": ["V1.1.1", "V1.1.2", ...],
  "notes": {
    "V1.1.1": "Verified via design review"
  }
}
```

### Print Report (Compliance Certificate)

**Use Case**: Generate printable compliance certificate for audits

**Trigger**: Click "Print Report" or `Ctrl+P`

**Output**: Multi-page PDF with:
- Executive summary (completion %)
- Category breakdown
- List of verified requirements with notes
- OWASP branding and license info

---

## 🔗 Deep Linking

Share specific requirements or filter states via URL:

### Link to Specific Requirement
```
https://owasp.org/.../isvs-tool/?req=V2.1.3
```
→ Opens tool with V2.1.3 highlighted and scrolled into view

### Link to Filtered View
```
https://owasp.org/.../isvs-tool/?level=L2&category=V4
```
→ Opens tool with L2 and V4 filters applied

### Copy Link Button
Each requirement has a "🔗 Share" button to copy its deep link.

---

## 🤝 Contributing

### Found a Bug?

1. Check [existing issues](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues)
2. If new, [open an issue](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues/new) with:
   - Browser and version
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)

### Feature Request?

1. [Open an issue](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues/new) with tag `enhancement`
2. Describe the use case and value proposition
3. Community will discuss and prioritize

### Want to Contribute Code?

1. See [DEVELOPMENT.md](./DEVELOPMENT.md) for setup
2. Fork the repository
3. Create a feature branch: `git checkout -b feature/my-feature`
4. Make changes with tests
5. Submit a pull request

**Coding Standards**:
- TypeScript strict mode
- ESLint + Prettier formatting
- Unit tests for utils (≥80% coverage)
- Accessibility compliance (WCAG 2.1 AA)

---

## 🐛 Troubleshooting

### Data Not Loading

**Symptom**: "Loading requirements..." never finishes

**Solution**:
1. Check browser console for errors
2. Verify `isvs-data.json` loads (Network tab)
3. Clear browser cache and reload

### Progress Not Saving

**Symptom**: Checked items reset after page reload

**Solution**:
1. Check localStorage is enabled (Settings → Privacy)
2. Verify storage quota not exceeded (unlikely with ~10 KB state)
3. Try exporting state as JSON, then re-importing

### Filters Not Working

**Symptom**: Filter checkboxes don't change displayed requirements

**Solution**:
1. Clear all filters and re-apply
2. Check browser console for JavaScript errors
3. Try incognito/private mode

### Export Button Not Working

**Symptom**: Click "Export CSV" but no file downloads

**Solution**:
1. Check browser's download settings
2. Disable popup blocker for `owasp.org`
3. Try "Export JSON" as alternative

### Mobile Display Issues

**Symptom**: Layout broken on mobile

**Solution**:
1. Ensure using modern mobile browser (Chrome/Safari latest)
2. Try landscape orientation
3. Report issue with device/browser details

---

## 📄 License

This tool is part of the OWASP ISVS project and is licensed under:

**[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**

You are free to:
- **Share** - Copy and redistribute the material
- **Adapt** - Remix, transform, and build upon the material

Under the following terms:
- **Attribution** - Give appropriate credit to OWASP
- **ShareAlike** - Distribute under the same license

---

## 📞 Support & Contact

### Project Leads

- **Cédric Bassem** - [cedric.bassem@owasp.org](mailto:cedric.bassem@owasp.org)
- **Aaron Guzman** - [aaron.guzman@owasp.org](mailto:aaron.guzman@owasp.org)

### Community

- **GitHub Issues**: [Report bugs or request features](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues)
- **OWASP Slack**: [#project-isvs](https://owasp.slack.com/messages/project-isvs) ([Join OWASP Slack](https://owasp.org/slack/invite))
- **Mailing List**: [Subscribe](https://groups.google.com/a/owasp.org/g/isvs-project)

### Documentation

- **Main ISVS Docs**: [https://owasp.org/IoT-Security-Verification-Standard-ISVS/](https://owasp.org/IoT-Security-Verification-Standard-ISVS/)
- **GitHub Repository**: [https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS)
- **OWASP Project Page**: [https://owasp.org/www-project-iot-security-verification-standard/](https://owasp.org/www-project-iot-security-verification-standard/)

---

## 🙏 Acknowledgments

Built with ❤️ by the OWASP community.

**Special Thanks**:
- OWASP ASVS team for Django app inspiration
- OWASP MASVS team for checklist UX patterns
- All ISVS contributors and reviewers

**Technology Credits**:
- React team for the amazing framework
- Vite team for blazing-fast builds
- Tailwind CSS for utility-first styling

---

**Version**: 1.0.0
**Last Updated**: October 2025
**Status**: Production Ready 🚀
