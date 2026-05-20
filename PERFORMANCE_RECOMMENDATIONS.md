# Performance Recommendations for RemoteObsidian

This document outlines performance optimizations and recommendations for this Obsidian vault repository.

## Implemented Improvements

### 1. Shell Script Optimization (obsidian_askpass.sh)

**Issue**: The script uses a busy-wait polling loop with a 0.1-second sleep interval, causing unnecessary CPU usage.

**Location**: `Project Skin/.obsidian/plugins/obsidian-git/obsidian_askpass.sh`

**Fix**: Increased sleep interval from 0.1s to 0.5s
- Reduces polling frequency by 80% (from 10 checks/second to 2 checks/second)
- Significantly decreases CPU usage during credential prompt operations
- Still provides responsive user experience (500ms delay is imperceptible)

**Impact**: Lower CPU usage, reduced battery drain, minimal impact on user experience

## Configuration Recommendations

### 2. Obsidian Git Plugin Settings

**Current Configuration** (`Project Skin/.obsidian/plugins/obsidian-git/data.json`):
- `autoSaveInterval`: 10 seconds
- `autoPullInterval`: 23 seconds  
- `autoPushInterval`: 25 seconds
- `refreshSourceControlTimer`: 7000ms (7 seconds)

**Recommendation**: Consider increasing these intervals for better performance:

```json
{
  "autoSaveInterval": 30,        // Reduce commits from every 10s to every 30s
  "autoPullInterval": 60,         // Reduce pulls from every 23s to every 60s
  "autoPushInterval": 60,         // Reduce pushes from every 25s to every 60s
  "refreshSourceControlTimer": 15000  // Reduce refreshes from 7s to 15s
}
```

**Benefits**:
- Reduces Git operations and network traffic
- Decreases disk I/O
- Improves battery life on mobile devices
- Still provides frequent enough backups (every 30 seconds)

**Trade-offs**: Slightly longer window for potential data loss (30s vs 10s), but still very safe for most use cases.

### 3. Large Plugin Alert

**Finding**: The `obsidian-annotator` plugin is 26MB in size, which may slow down vault initialization.

**Recommendation**: 
- If PDF annotation features are not frequently used, consider disabling this plugin
- Only enable when needed for specific tasks
- Monitor vault loading times if experiencing slowness

## Additional Performance Tips

1. **Regular Cleanup**: Periodically review and remove unused plugins to reduce vault size and loading time

2. **Optimize Auto-backup**: If working with large vaults, consider using `autoBackupAfterFileChange: false` and rely on interval-based backups instead

3. **Mobile Performance**: On mobile devices, further increase the intervals above to conserve battery and reduce background processing

4. **Network Considerations**: If on slow/metered connection, increase pull/push intervals significantly or disable auto-sync

## Monitoring Performance

Watch for these indicators of performance issues:
- Vault taking >3 seconds to load
- UI lag when typing
- High CPU usage when idle
- Frequent git operations in background
- Battery draining faster than expected

If experiencing these issues, start by increasing the git plugin intervals and disabling unused plugins.

## Summary of Changes

| Component | Before | After | Improvement |
|-----------|--------|-------|-------------|
| obsidian_askpass.sh polling | 0.1s (10/sec) | 0.5s (2/sec) | 80% fewer polls |

**Recommended** (not auto-applied):
| Setting | Current | Recommended | Benefit |
|---------|---------|-------------|---------|
| autoSaveInterval | 10s | 30s | 67% fewer commits |
| autoPullInterval | 23s | 60s | 61% fewer pulls |
| autoPushInterval | 25s | 60s | 58% fewer pushes |
| refreshSourceControl | 7s | 15s | 53% fewer refreshes |
