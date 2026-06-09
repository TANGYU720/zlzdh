<template>
  <div class="about">
    <section class="about-header">
      <div class="container">
        <h2>关于我们</h2>
        <p>了解我们的企业和团队</p>
      </div>
    </section>
    
    <section class="company-info">
      <div class="container">
        <div class="info-grid">
          <div class="info-item">
            <h3>企业简介</h3>
            <p>我们是一家专注于企业服务领域的专业公司，成立于2010年。多年来，我们始终坚持以客户为中心，以创新为动力，不断提升服务品质，赢得了广大客户的信赖和好评。</p>
            <p>我们的使命是帮助企业实现数字化转型，提升核心竞争力，共创美好未来。</p>
          </div>
          <div class="info-item">
            <h3>发展历程</h3>
            <ul>
              <li><strong>2010年</strong> - 公司成立，开始提供企业咨询服务</li>
              <li><strong>2015年</strong> - 拓展业务范围，进入技术服务领域</li>
              <li><strong>2020年</strong> - 完成数字化转型，推出在线服务平台</li>
              <li><strong>2026年</strong> - 成为行业领先的综合服务提供商</li>
            </ul>
          </div>
        </div>
      </div>
    </section>
    
    <section class="team">
      <div class="container">
        <h3>核心团队</h3>
        <div class="team-grid">
          <div class="team-member">
            <div class="avatar">👨‍💼</div>
            <h4>张明</h4>
            <p>CEO / 创始人</p>
            <p>拥有20年企业管理经验</p>
          </div>
          <div class="team-member">
            <div class="avatar">👩‍💼</div>
            <h4>李华</h4>
            <p>CTO</p>
            <p>资深技术专家，带领团队创新发展</p>
          </div>
          <div class="team-member">
            <div class="avatar">👨‍💼</div>
            <h4>王强</h4>
            <p>COO</p>
            <p>负责公司运营管理</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.about-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
  padding: 60px 0;
}

.about-header h2 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.about-header p {
  font-size: 1.2rem;
}

.company-info {
  padding: 60px 0;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 40px;
}

.info-item h3 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #2c3e50;
}

.info-item p {
  margin-bottom: 15px;
  color: #666;
  line-height: 1.8;
}

.info-item ul {
  list-style: none;
}

.info-item li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.team {
  padding: 60px 0;
  background-color: #f8f9fa;
}

.team h3 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
}

.team-member {
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.avatar {
  font-size: 4rem;
  margin-bottom: 15px;
}

.team-member h4 {
  font-size: 1.3rem;
  margin-bottom: 5px;
}

.team-member p {
  color: #666;
  margin-bottom: 5px;
}
</style>
