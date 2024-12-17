---
title: Appcircle Documentation
description: Explore Appcircle Documentation, a comprehensive guide for building, testing, and deploying your mobile applications.
tags: [appcircle, documentation, build, test, deploy]
sidebar_position: 1
slug: /
hide_table_of_contents: true
hide_title: true
breadcrumbs: false
---

import NewBadge from '@site/src/components/NewBadge';
import PublishIcon from "@site/src/components/ModuleIcons/PublishIcon";
import SigningIdentitiesIcon from "@site/src/components/ModuleIcons/SigningIdentitiesIcon";
import BuildIcon from "@site/src/components/ModuleIcons/BuildIcon";
import DistributeIcon from "@site/src/components/ModuleIcons/DistributeIcon";

<div class="intro-visual">

<div class="intro-text"><h5 class="intro-visual-header">
Build.<br/>Test.<br/>Distribute.
</h5>
<p>Make better, safer mobile app releases with Appcircle.</p>
</div>
<div className="intro-image"><img src="https://cdn.appcircle.io/docs/assets/docs-intro-header.png" alt="Intro Header" /></div>
</div>

<section class="intro-cards">
      <div class="intro-card">
            <h3><a href="/build/platform-build-guides">Platform Build Guides</a></h3>
            <p><strong>New to Appcircle?</strong> Get started by adding your Obj-C/Swift, Java/Kotlin, React Native, Flutter app first.</p>
      </div>
      <div class="intro-card">
            <h3><a href="/build/manage-the-connections/adding-a-build-profile">Building Your Apps</a></h3>
            <p>Learn about setting up your repository, creating workflows and how to automatically trigger a build.</p>
      </div>
      <div class="intro-card">
            <h3><a href="/publish-module">Send to Testers & Stores</a></h3>
            <p>Add testers, set up your builds to be auto distributed to them and Apple App Store, Testflight, Google Play, Huawei AppGallery and Firebase.</p>
      </div>
      <div class="intro-card">
            <h3><a href="/continuous-testing">Running Unit & UI Tests</a></h3>
            <p>Learn how to run Unit and UI tests and see detailed reports on which ones have failed and why.</p>
      </div>
</section>

<section class="feature-cards">
<div class="build-mobile-stack">
    <div className="feature-card-image">
       <BuildIcon width="70" height="70" fill="#ff8114" />
    </div>
    <div className="feature-card-info">
        <h4>Build</h4>
        <p>Supports major mobile stacks including native and cross-platform frameworks. Seamless integration with popular Git providers like GitHub, BitBucket, and GitLab.</p>
        <p>Customizable workflows with automated processes and secure environment management.</p>
        <p>Advanced caching, versioning, and real-time build insights with detailed dashboards.</p>
    </div>
           <a href="/build" className="feature-card-learn-more build">
            <span>Learn how</span>
        </a>
</div>

<div class="signing-identities-card">
    <div className="feature-card-image">
            <SigningIdentitiesIcon width="70" height="70" fill="#ff8114" />
    </div>
    <div className="feature-card-info">
        <h4>Signing Identities</h4>
        <p>Manage iOS certificates and Android keystores centrally & securely, accessible across multiple projects.</p>
        <p>Automate certificate and provisioning profile management with App Store Connect integration.</p>
        <p>Receive notifications for expiring certificates and track signing activities with detailed audits.</p>
    </div>
         <a href="/signing-identities" className="feature-card-learn-more signing">
            <span>Learn how</span>
        </a>
</div>

<div class="testing-distribution-card">
    <div className="feature-card-image">
            <DistributeIcon width="70" height="70" fill="#ff8114" />
    </div>
    <div className="feature-card-info">
        <h4>Testing Distribution</h4>
  <p>Distribute app builds via email, QR codes, and webhooks. Share .IPA, APK, and other file formats directly.</p>

        <p>Create test groups, automate distribution, and integrate with DevOps pipelines.</p>

        <p>Securely manage test groups with LDAP/SSO (OpenID & SAML) and track engagement with detailed reports.</p>
    </div>
          <a href="/testing-distribution" className="feature-card-learn-more testing">
             <span>Learn how</span>
        </a>

</div>

<div class="publish-to-stores-card">
    <div className="feature-card-image">
            <PublishIcon width="70" height="70" fill="#ff8114" />
    </div>
    <div className="feature-card-info">
        <h4>Publish</h4>
        <p>Publish apps to App Store, Google Play, and Huawei AppGallery from a single module. Automate the process with customizable workflows.</p>

        <p>Track release performance with audit logs and reports, and update metadata like descriptions, keywords, and screenshots.</p>

        <p>Deploy to multiple platforms like App Store, TestFlight, Google Play, and more, with phased rollouts and version management support.</p>
    </div>
            <a href="/publish-module" className="feature-card-learn-more publish">
             <span>Learn how</span>
        </a>

</div>

      <div class="enterprise-app-store">
            <div className="feature-card-image"><img src="https://cdn.appcircle.io/docs/assets/feature-card-eas.png" alt="Feature Card" /></div>
            <div className="feature-card-info">
                  <h4>Create your own app store.</h4>
                  <p>Some apps are not meant to be on App Stores. That’s why we’re introducing Enterprise App Store. A way for you to distribute your internal apps.</p>

            </div>
                 <a href="/enterprise-app-store/enterprise-app-store-profile" className="feature-card-learn-more eas">
                         <span>Learn how</span>
                  </a>
      </div>
      <div class="self-hosted-runners">
            <div className="feature-card-image"><img src="https://cdn.appcircle.io/docs/assets/feature-card-self-hosted-runners.png" alt="Feature Card Self Hosted" /></div>
            <div className="feature-card-info">
                  <h4>Self-Hosted Appcircle</h4>
                  <p>Want to use your own build machines? Just install our runner scripts to the machines you want to use for your iOS / Android builds.</p>

            </div>
                  <a href="/self-hosted-appcircle" className="feature-card-learn-more runner">
                        <span>Learn how</span>
                  </a>
      </div>

</section>

## Dive Deeper into Appcircle

<section class="community">
<a class="slack" href="https://slack.appcircle.io">
<img src="https://cdn.appcircle.io/docs/assets/slack-logo.png" alt="Slack Logo" />
<span>Slack Community</span>
</a>
<a class="videos" href="https://www.youtube.com/c/Appcircle">
<img src="https://cdn.appcircle.io/docs/assets/youtube-logo.png" alt="Youtube Logo" />
<span>How-To Videos</span>
</a>

<a class="twitter" href="https://twitter.com/appcircleio">
 <svg width="41" height="34" viewBox="0 0 41 34" fill="none" xmlns="http://www.w3.org/2000/svg" {...props}>
      <path d="M36.6933 8.54828C36.7181 8.90995 36.7181 9.27162 36.7181 9.63662C36.7181 20.7583 28.3197 33.5849 12.9629 33.5849V33.5783C8.42645 33.5849 3.98423 32.275 0.165283 29.805C0.82492 29.885 1.48786 29.9249 2.15246 29.9266C5.9119 29.9299 9.56387 28.6583 12.5215 26.3166C8.94887 26.2483 5.81601 23.9 4.72157 20.4716C5.97306 20.715 7.26258 20.6649 8.49093 20.3266C4.59593 19.5333 1.79371 16.0833 1.79371 12.0766C1.79371 12.0399 1.79371 12.0049 1.79371 11.9699C2.95428 12.6216 4.25371 12.9833 5.5829 13.0233C1.9144 10.5516 0.78359 5.63162 2.99891 1.78495C7.23778 7.04328 13.4919 10.2399 20.2057 10.5783C19.5328 7.65495 20.452 4.59162 22.621 2.53662C25.9837 -0.650051 31.2724 -0.486718 34.4333 2.90162C36.3031 2.52995 38.0952 1.83828 39.7352 0.858283C39.112 2.80662 37.8076 4.46162 36.0651 5.51328C37.72 5.31662 39.3368 4.86995 40.8594 4.18828C39.7385 5.88162 38.3267 7.35662 36.6933 8.54828Z" fill="#1ea1f2" />
</svg>
<span>Follow us on Twitter</span>
</a>

<a class="contact-us" href="https://appcircle.io/contact">
<img src="https://cdn.appcircle.io/docs/assets/contact-us-logo.png" alt="Contact Us Logo" />
<span>Contact Us</span>
</a>

</section>

### See something that's not documented here?

Send us a request and we will get it in: [Appcircle Support](https://appcircle.io/support/)
