# 📦 Project Deliverables Checklist

## 🔗 Links

### DockerHub Repository
- **URL**: https://hub.docker.com/r/YOUR_USERNAME/taskmanager
- **Image**: `YOUR_USERNAME/taskmanager:latest`

### GitHub Repository
- **URL**: https://github.com/adem951/lab_ml_prod_dockerhub
- **CI/CD Workflow**: https://github.com/adem951/lab_ml_prod_dockerhub/actions

---

## 📸 Screenshots Required

### 1. DockerHub - Image Pushed
**Where to capture**:
- Go to: https://hub.docker.com/r/YOUR_USERNAME/taskmanager/tags
- Screenshot showing:
  - ✅ Image name: `taskmanager`
  - ✅ Tags: `latest`, `main-xxxxx`, timestamp
  - ✅ Push timestamp
  - ✅ Image size

### 2. GitHub Actions - Successful CI/CD Pipeline
**Where to capture**:
- Go to: https://github.com/adem951/lab_ml_prod_dockerhub/actions
- Screenshot showing:
  - ✅ Workflow name: "CI/CD Pipeline"
  - ✅ Green checkmark (success)
  - ✅ All jobs passed (lint-and-test, build-validation, build-and-push)
  - ✅ Timestamp of run

---

## 🎥 Video Recording Checklist

**Duration**: 2-5 minutes

**Tools**: Loom, OBS Studio, Windows Game Bar (Win+G)

**What to show**:
1. ✅ **Code push** (30s)
   - Show terminal with `git push origin main`
   - Show commit message

2. ✅ **GitHub Actions running** (1-2 min)
   - Open: https://github.com/adem951/lab_ml_prod_dockerhub/actions
   - Show workflow running (yellow dots)
   - Wait or fast-forward to completion (green checkmarks)
   - Click on workflow to show job details

3. ✅ **DockerHub verification** (30s)
   - Open: https://hub.docker.com/r/YOUR_USERNAME/taskmanager
   - Show the new image with tags
   - Show push timestamp matching CI/CD run

---

## 📄 Document Structure

### PDF/Word Document should include:

1. **Cover Page**
   - Project Title: "ML Production - Docker & CI/CD Lab"
   - Your Name
   - Date

2. **Section 1: Repository Links**
   - DockerHub URL
   - GitHub URL

3. **Section 2: Screenshots**
   - Screenshot 1: DockerHub with pushed image
   - Screenshot 2: GitHub Actions successful pipeline

4. **Section 3: Video Link**
   - Loom/YouTube link to your demo video

5. **Section 4: Conclusion**
   - Brief summary (2-3 sentences)

---

## ✅ Verification Commands

### Check Docker image locally:
```bash
docker pull YOUR_USERNAME/taskmanager:latest
docker run -d -p 5000:5000 -e SECRET_KEY="test" -e DATABASE_URL="postgresql://..." YOUR_USERNAME/taskmanager:latest
```

### Check GitHub Actions status:
```bash
# View in browser
https://github.com/adem951/lab_ml_prod_dockerhub/actions
```
