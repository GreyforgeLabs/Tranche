const repository = "https://github.com/blackopsrepl/Tranche";
const version = { filename: "VERSION", type: "plain-text" };

module.exports = {
  packageFiles: [version],
  bumpFiles: [version],
  tagPrefix: "v",
  releaseCommitMessageFormat: "chore(release): {{currentTag}}",
  commitUrlFormat: `${repository}/commit/{{hash}}`,
  compareUrlFormat: `${repository}/compare/{{previousTag}}...{{currentTag}}`,
  issueUrlFormat: `${repository}/issues/{{id}}`,
  scripts: { prerelease: "make release-check" },
};
