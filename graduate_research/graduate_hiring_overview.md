# Graduate Hiring Overview

This document details the methodology, sources, and findings from our research into new graduate hiring trends at major Japanese IT companies from 2020 to 2023.

## Data Collection Methodology

### Sources Used
1. **Annual Reports (統合報告書)**
   - Official company financial reports
   - Most reliable source for historical data
   - Often includes breakdowns of hiring by job category

2. **Press Releases (プレスリリース)**
   - Announcements of hiring plans and results
   - Timely information about recruitment targets
   - Sometimes includes detailed breakdowns

3. **Career Pages (採用情報)**
   - Current recruitment information
   - Historical hiring data
   - Job category details

4. **IR Reports (投資家向け情報)**
   - Quarterly/annual financial presentations
   - Employee-related metrics
   - Strategic hiring initiatives

### Data Coverage
- **Time Period**: 2020-2023
- **Companies**:
  - Rakuten (楽天グループ)
  - CyberAgent (サイバーエージェント)
  - DeNA
  - LINE
  - SoftBank
  - NTT Data
  - Fujitsu (富士通)

## Key Findings

### Hiring Trends
1. **Overall Growth**
   - Most companies show steady increase in new graduate hiring
   - Rakuten shows consistent growth from 530 (2020) to 700 (2023)
   - CyberAgent increased from 417 (2020) to 483 (2022)

2. **Technical Hiring Focus**
   - Strong emphasis on engineering/technical roles
   - Rakuten: Engineering hires increased from ~200 (2020) to ~320 (2023)
   - LINE: ~60% engineering hires in 2021
   - NTT Data: ~75% technical hires consistently

3. **Company-Specific Trends**
   - SoftBank shows largest hiring numbers (1200-1300) but includes group companies
   - Fujitsu emphasizes digital talent (~500 of 750 hires in 2021)
   - DeNA maintains steady technical focus (~100 of 215 hires in 2020)

## Data Collection Details

### Data Format
The data is stored in CSV format with the following columns:
- company: Company name
- year: Hiring year
- new_grads_hired: Number of new graduates hired
- notes: Additional context (job categories, etc.)
- source: Data source type

### Assumptions and Notes
1. **Hiring Numbers**
   - When ranges were given, we used the middle value
   - Group company numbers (e.g., SoftBank) include all subsidiaries
   - Technical hire percentages are approximate when exact numbers weren't provided

2. **Time Periods**
   - Fiscal years are used (typically April-March)
   - Some 2023 data may be planned rather than actual numbers

3. **Job Categories**
   - "Technical" and "Engineering" roles may have different definitions by company
   - Digital talent includes both software and digital transformation roles
   - Some companies don't provide detailed breakdowns

## Data Reliability
- Most reliable: Annual Report data (audited numbers)
- Very reliable: Press Release data (official announcements)
- Reliable: Career Page data (may include plans rather than actual numbers)
- Cross-referenced: Multiple sources used when available

## Future Updates
To maintain and update this dataset:
1. Check annual reports each May-June
2. Monitor press releases during recruitment season (June-March)
3. Verify numbers against career page announcements
4. Update both CSV and documentation with new findings

## Reference
The complete dataset can be found in [graduate_hiring_trends.csv](graduate_hiring_trends.csv).
