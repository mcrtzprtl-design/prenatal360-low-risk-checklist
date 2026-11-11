// Education-only gestational week calculator
function gestationalWeek(lmp, today){ const d = (new Date(today)-new Date(lmp))/86400000; return Math.max(0, Math.min(42, Math.floor(d/7))); }
console.log(gestationalWeek("2026-08-01","2026-11-11"));
