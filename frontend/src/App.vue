<template>
  <div class="app">
    <nav class="navbar">
      <div class="container">
        <div class="logo">
          <svg class="logo-icon" viewBox="0 0 60 40" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="tyGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#06b6d4"/>
                <stop offset="100%" style="stop-color:#3b82f6"/>
              </linearGradient>
              <linearGradient id="tyGradientLight" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#22d3ee"/>
                <stop offset="100%" style="stop-color:#06b6d4"/>
              </linearGradient>
            </defs>
            <rect x="8" y="8" width="8" height="24" rx="1.5" fill="url(#tyGradient)"/>
            <rect x="8" y="8" width="22" height="6" rx="1.5" fill="url(#tyGradient)"/>
            <rect x="8" y="16" width="14" height="4" rx="1" fill="url(#tyGradientLight)"/>
            <polygon points="35,8 35,32 52,20" fill="none" stroke="url(#tyGradient)" stroke-width="7" stroke-linejoin="round"/>
            <circle cx="50" cy="30" r="3" fill="url(#tyGradientLight)"/>
            <circle cx="32" cy="6" r="2" fill="#06b6d4">
              <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
            </circle>
            <circle cx="54" cy="10" r="1.5" fill="#3b82f6">
              <animate attributeName="opacity" values="0.8;0.2;0.8" dur="2s" repeatCount="indefinite"/>
            </circle>
          </svg>
          <span class="logo-text">智联自动化</span>
        </div>
        <ul class="nav-links">
          <li><router-link to="/" :class="{ active: $route.name === 'Home' }">首页</router-link></li>
          <li><router-link to="/news" :class="{ active: $route.name === 'News' }">行业资讯</router-link></li>
          <li><router-link to="/cases" :class="{ active: $route.name === 'Cases' }">项目案例</router-link></li>
          <li><router-link to="/tutorials" :class="{ active: $route.name === 'Tutorials' }">技术教程</router-link></li>
          <li><router-link to="/downloads" :class="{ active: $route.name === 'Downloads' }">资源下载</router-link></li>
          <li><router-link to="/contact" :class="{ active: $route.name === 'Contact' }">联系我们</router-link></li>
        </ul>
        <div class="nav-toggle" @click="toggleMenu">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </nav>
    <main>
      <router-view />
    </main>
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h4>关于我们</h4>
            <p>智联自动化致力于为制造业提供领先的工业4.0解决方案，推动企业数字化转型。</p>
          </div>
          <div class="footer-section">
            <h4>快速链接</h4>
            <ul>
              <li><router-link to="/">首页</router-link></li>
              <li><router-link to="/news">行业资讯</router-link></li>
              <li><router-link to="/cases">项目案例</router-link></li>
              <li><router-link to="/contact">联系我们</router-link></li>
            </ul>
          </div>
          <div class="footer-section">
            <h4>联系方式</h4>
            <p>📞 400-888-8888</p>
            <p>✉️ contact@zhilian-auto.com</p>
            <p>📍 上海市浦东新区张江高科技园区</p>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2026 智联自动化科技有限公司. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', 'PingFang SC', -apple-system, BlinkMacSystemFont, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f7fa;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.navbar {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: white;
  padding: 1rem 0;
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  font-weight: bold;
}

.logo-icon {
  width: 50px;
  height: 35px;
  margin-right: 10px;
}

.logo-text {
  background: linear-gradient(135deg, #06b6d4, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.nav-links {
  display: flex;
  list-style: none;
}

.nav-links li {
  margin-left: 2rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  position: relative;
}

.nav-links a:hover,
.nav-links a.active {
  color: #06b6d4;
}

.nav-links a.active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, #06b6d4, #3b82f6);
  border-radius: 2px;
}

.nav-toggle {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.nav-toggle span {
  width: 25px;
  height: 3px;
  background: white;
  margin: 3px 0;
  transition: all 0.3s;
}

main {
  padding-top: 80px;
  min-height: calc(100vh - 200px);
}

.footer {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: white;
  padding: 3rem 0;
  margin-top: 3rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section h4 {
  margin-bottom: 1rem;
  color: #06b6d4;
}

.footer-section p {
  color: #94a3b8;
  margin-bottom: 0.5rem;
}

.footer-section ul {
  list-style: none;
}

.footer-section ul li {
  margin-bottom: 0.5rem;
}

.footer-section ul li a {
  color: #94a3b8;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-section ul li a:hover {
  color: #06b6d4;
}

.footer-bottom {
  border-top: 1px solid #334155;
  padding-top: 1rem;
  text-align: center;
  color: #64748b;
}

@media (max-width: 768px) {
  .nav-links {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    padding: 1rem 0;
  }
  
  .nav-links li {
    margin: 0.5rem 2rem;
  }
  
  .nav-toggle {
    display: flex;
  }
  
  .nav-links.active {
    display: flex;
  }
}
</style>
