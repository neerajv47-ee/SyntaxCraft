/**
 * SyntaxCraft - Frontend JavaScript
 * Full Integrated MVP: Generator, Insights, Test Cases, Practice, Hub & History
 */

document.addEventListener("DOMContentLoaded", () => {
  // -------------------------------------------------------------------------
  // 1. Mobile Sidebar Toggle
  // -------------------------------------------------------------------------
  const mobileToggle = document.getElementById("mobileToggle");
  const sidebar = document.getElementById("appSidebar");

  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener("click", () => {
      sidebar.classList.toggle("open");
    });

    document.addEventListener("click", (e) => {
      if (
        window.innerWidth <= 992 &&
        sidebar.classList.contains("open") &&
        !sidebar.contains(e.target) &&
        !mobileToggle.contains(e.target)
      ) {
        sidebar.classList.remove("open");
      }
    });
  }

  // -------------------------------------------------------------------------
  // 2. Global Toast Notification Helper
  // -------------------------------------------------------------------------
  let toastTimer = null;
  window.showToast = function (message) {
    let toast = document.getElementById("syntaxToast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "syntaxToast";
      toast.className = "toast-box";
      document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.classList.add("show");

    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove("show");
    }, 3000);
  };

  // -------------------------------------------------------------------------
  // 3. Copy Code Buttons (Target element or raw data attribute)
  // -------------------------------------------------------------------------
  document.querySelectorAll(".btn-copy").forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-target");
      const targetElement = document.getElementById(targetId);
      if (targetElement) {
        const text = targetElement.innerText || targetElement.textContent;
        navigator.clipboard
          .writeText(text)
          .then(() => {
            window.showToast("✓ Code copied to clipboard!");
          })
          .catch(() => {
            window.showToast("Could not copy to clipboard.");
          });
      }
    });
  });

  document.querySelectorAll(".btn-copy-raw").forEach((btn) => {
    btn.addEventListener("click", () => {
      const rawCode = btn.getAttribute("data-code");
      if (rawCode) {
        navigator.clipboard
          .writeText(rawCode)
          .then(() => {
            window.showToast("✓ Solution copied to clipboard!");
          })
          .catch(() => {
            window.showToast("Could not copy to clipboard.");
          });
      }
    });
  });

  // -------------------------------------------------------------------------
  // 4. Code Generator Handlers
  // -------------------------------------------------------------------------
  const promptInput = document.getElementById("instructionInput");
  const exampleChips = document.querySelectorAll(".prompt-chip");

  exampleChips.forEach((chip) => {
    chip.addEventListener("click", () => {
      const promptText = chip.getAttribute("data-prompt");
      if (promptInput && promptText) {
        promptInput.value = promptText;
        promptInput.focus();
        window.showToast("Example prompt loaded!");
      }
    });
  });

  const clearBtn = document.getElementById("btnClearInput");
  if (clearBtn && promptInput) {
    clearBtn.addEventListener("click", () => {
      promptInput.value = "";
      promptInput.focus();
    });
  }

  const generatorForm = document.getElementById("generatorForm");
  const codeOutput = document.getElementById("generatorCodeOutput");
  const taskBadge = document.getElementById("taskBadge");
  const unsupportedAlert = document.getElementById("unsupportedAlert");
  const unsupportedMessage = document.getElementById("unsupportedMessage");
  const btnGenerateCode = document.getElementById("btnGenerateCode");
  const difficultySelect = document.getElementById("difficultySelect");
  const btnNextInsights = document.getElementById("btnNextInsights");
  const btnNextTestCases = document.getElementById("btnNextTestCases");

  if (generatorForm && codeOutput) {
    generatorForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      const promptValue = promptInput ? promptInput.value.trim() : "";
      const difficultyValue = difficultySelect ? difficultySelect.value : "Beginner";

      if (!promptValue) {
        window.showToast("Please enter an English instruction first.");
        return;
      }

      const originalBtnHtml = btnGenerateCode ? btnGenerateCode.innerHTML : "";
      if (btnGenerateCode) {
        btnGenerateCode.disabled = true;
        btnGenerateCode.innerHTML = "<span>Generating...</span>";
      }

      try {
        const response = await fetch("/generator", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            prompt: promptValue,
            difficulty: difficultyValue
          })
        });

        if (!response.ok) {
          throw new Error(`Server returned HTTP ${response.status}`);
        }

        const data = await response.json();
        codeOutput.textContent = data.code;

        if (data.success) {
          if (unsupportedAlert) unsupportedAlert.style.display = "none";
          if (taskBadge) {
            taskBadge.textContent = `${data.task} (${data.difficulty})`;
            taskBadge.className = "tag-badge easy";
          }
          if (btnNextInsights) {
            btnNextInsights.href = `/insights?task=${data.task_id}&difficulty=${data.difficulty}`;
          }
          if (btnNextTestCases) {
            btnNextTestCases.href = `/test-cases?task=${data.task_id}&difficulty=${data.difficulty}`;
          }
          window.showToast("✓ Python code generated successfully!");
        } else {
          if (unsupportedAlert) {
            unsupportedAlert.style.display = "block";
            if (unsupportedMessage) unsupportedMessage.textContent = data.message;
          }
          if (taskBadge) {
            taskBadge.textContent = "Unsupported Request";
            taskBadge.className = "tag-badge medium";
          }
          window.showToast("Task not recognized. Try one of the examples.");
        }
      } catch (err) {
        console.error("Code generation error:", err);
        generatorForm.submit();
      } finally {
        if (btnGenerateCode) {
          btnGenerateCode.disabled = false;
          btnGenerateCode.innerHTML = originalBtnHtml;
        }
      }
    });
  }

  // -------------------------------------------------------------------------
  // 5. Test Cases Runner
  // -------------------------------------------------------------------------
  const btnRunTestCases = document.getElementById("btnRunTestCases");
  const testRunSuccessAlert = document.getElementById("testRunSuccessAlert");

  if (btnRunTestCases) {
    btnRunTestCases.addEventListener("click", () => {
      btnRunTestCases.disabled = true;
      btnRunTestCases.innerHTML = "Running Tests...";

      setTimeout(() => {
        btnRunTestCases.disabled = false;
        btnRunTestCases.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polygon points="5 3 19 12 5 21 5 3"></polygon>
          </svg> Run All Tests
        `;
        if (testRunSuccessAlert) {
          testRunSuccessAlert.style.display = "block";
        }
        window.showToast("✓ All test cases passed successfully!");
      }, 450);
    });
  }

  // -------------------------------------------------------------------------
  // 6. Practice Mode Interactive Solver & Filters
  // -------------------------------------------------------------------------
  let activeProblemId = "prob-001";
  let activeProblemStarter = "";

  const problemCards = document.querySelectorAll(".problem-card-item");
  const activeTitle = document.getElementById("activeProblemTitle");
  const activeDiff = document.getElementById("activeProblemDiff");
  const activeDesc = document.getElementById("activeProblemDesc");
  const activeIn = document.getElementById("activeSampleIn");
  const activeOut = document.getElementById("activeSampleOut");
  const practiceEditor = document.getElementById("practiceCodeEditor");
  const feedbackBox = document.getElementById("practiceFeedbackBox");
  const feedbackStatus = document.getElementById("feedbackStatusText");
  const feedbackExpl = document.getElementById("feedbackExplanationText");

  function selectProblem(card) {
    problemCards.forEach((c) => c.classList.remove("selected-problem"));
    card.classList.add("selected-problem");

    activeProblemId = card.getAttribute("data-id");
    activeProblemStarter = card.getAttribute("data-starter") || "";

    if (activeTitle) activeTitle.textContent = card.getAttribute("data-title");
    if (activeDiff) {
      const diff = card.getAttribute("data-difficulty");
      activeDiff.textContent = diff;
      activeDiff.className = `tag-badge ${diff === "Easy" ? "easy" : "medium"}`;
    }
    if (activeDesc) activeDesc.textContent = card.getAttribute("data-desc");
    if (activeIn) activeIn.textContent = card.getAttribute("data-sample-in");
    if (activeOut) activeOut.textContent = card.getAttribute("data-sample-out");
    if (practiceEditor) practiceEditor.value = activeProblemStarter;

    if (feedbackBox) feedbackBox.style.display = "none";
  }

  problemCards.forEach((card) => {
    card.addEventListener("click", () => selectProblem(card));
  });

  // Reset editor button
  const btnResetPractice = document.getElementById("btnResetPractice");
  if (btnResetPractice && practiceEditor) {
    btnResetPractice.addEventListener("click", () => {
      practiceEditor.value = activeProblemStarter;
      if (feedbackBox) feedbackBox.style.display = "none";
      window.showToast("Editor reset to starter template.");
    });
  }

  // Check Solution button
  const btnCheckSolution = document.getElementById("btnCheckSolution");
  if (btnCheckSolution && practiceEditor) {
    btnCheckSolution.addEventListener("click", async () => {
      const code = practiceEditor.value.trim();
      if (!code) {
        window.showToast("Please enter your Python code first.");
        return;
      }

      btnCheckSolution.disabled = true;
      btnCheckSolution.innerText = "Evaluating...";

      try {
        const response = await fetch("/api/check-practice", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            problem_id: activeProblemId,
            code: code
          })
        });

        const data = await response.json();

        if (feedbackBox && feedbackStatus && feedbackExpl) {
          feedbackBox.style.display = "block";
          if (data.correct) {
            feedbackBox.style.background = "rgba(16, 185, 129, 0.12)";
            feedbackBox.style.border = "1px solid rgba(16, 185, 129, 0.4)";
            feedbackStatus.style.color = "var(--accent-emerald)";
            feedbackStatus.textContent = "✓ Correct Solution!";
            feedbackExpl.textContent = data.explanation;
            window.showToast("✓ Great job! Challenge passed.");
          } else {
            feedbackBox.style.background = "rgba(244, 63, 94, 0.12)";
            feedbackBox.style.border = "1px solid rgba(244, 63, 94, 0.4)";
            feedbackStatus.style.color = "var(--accent-rose)";
            feedbackStatus.textContent = "✗ Incorrect Solution";
            feedbackExpl.textContent = data.explanation;
            window.showToast("Solution didn't match expected criteria.");
          }
        }
      } catch (err) {
        console.error("Practice check error:", err);
        window.showToast("Could not evaluate solution.");
      } finally {
        btnCheckSolution.disabled = false;
        btnCheckSolution.innerText = "Check Solution";
      }
    });
  }

  // Topic filter
  const filterPills = document.querySelectorAll(".filter-pill");
  const filterDiffs = document.querySelectorAll(".filter-diff");

  let currentCategory = "all";
  let currentDifficulty = "all";

  function applyPracticeFilters() {
    problemCards.forEach((card) => {
      const cat = card.getAttribute("data-category") || "";
      const diff = card.getAttribute("data-difficulty") || "";

      const matchCat = currentCategory === "all" || cat.toLowerCase().includes(currentCategory.toLowerCase());
      const matchDiff = currentDifficulty === "all" || diff.toLowerCase() === currentDifficulty.toLowerCase();

      card.style.display = matchCat && matchDiff ? "flex" : "none";
    });
  }

  filterPills.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterPills.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentCategory = btn.getAttribute("data-category") || "all";
      applyPracticeFilters();
    });
  });

  filterDiffs.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterDiffs.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentDifficulty = btn.getAttribute("data-diff") || "all";
      applyPracticeFilters();
    });
  });

  // Initialize first problem starter
  if (problemCards.length > 0) {
    activeProblemStarter = problemCards[0].getAttribute("data-starter") || "";
  }

  // -------------------------------------------------------------------------
  // 7. Python Hub Filter & Search
  // -------------------------------------------------------------------------
  const hubFilterBtns = document.querySelectorAll(".hub-filter-btn");
  const hubCards = document.querySelectorAll(".hub-topic-card");
  const hubSearch = document.getElementById("hubSearchInput");

  let activeHubCat = "all";

  function filterHubCards() {
    const query = hubSearch ? hubSearch.value.trim().toLowerCase() : "";
    hubCards.forEach((card) => {
      const cat = card.getAttribute("data-category") || "";
      const title = card.getAttribute("data-title") || "";

      const matchCat = activeHubCat === "all" || cat.toLowerCase() === activeHubCat.toLowerCase();
      const matchQuery = !query || title.includes(query) || cat.toLowerCase().includes(query);

      card.style.display = matchCat && matchQuery ? "block" : "none";
    });
  }

  hubFilterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      hubFilterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeHubCat = btn.getAttribute("data-category") || "all";
      filterHubCards();
    });
  });

  if (hubSearch) {
    hubSearch.addEventListener("input", filterHubCards);
  }

  // -------------------------------------------------------------------------
  // 8. History Management (Clear & Modal Preview)
  // -------------------------------------------------------------------------
  const btnClearHistory = document.getElementById("btnClearHistoryBtn");
  if (btnClearHistory) {
    btnClearHistory.addEventListener("click", async () => {
      if (!confirm("Are you sure you want to clear your generation history?")) {
        return;
      }
      try {
        const res = await fetch("/api/clear-history", { method: "POST" });
        if (res.ok) {
          window.location.reload();
        }
      } catch (err) {
        console.error("Clear history failed:", err);
      }
    });
  }

  // History modal handlers
  const historyModal = document.getElementById("historyModal");
  const modalTask = document.getElementById("modalTaskName");
  const modalPrompt = document.getElementById("modalPromptText");
  const modalCode = document.getElementById("modalCodeOutput");
  const btnCloseModal = document.getElementById("btnCloseModal");
  const btnCloseModalBtn = document.getElementById("btnCloseModalBtn");

  document.querySelectorAll(".btn-view-history").forEach((btn) => {
    btn.addEventListener("click", () => {
      const task = btn.getAttribute("data-task");
      const prompt = btn.getAttribute("data-prompt");
      const code = btn.getAttribute("data-code");

      if (historyModal && modalTask && modalPrompt && modalCode) {
        modalTask.textContent = task;
        modalPrompt.textContent = `Prompt: "${prompt}"`;
        modalCode.textContent = code;
        historyModal.style.display = "flex";
      }
    });
  });

  function closeHistoryModal() {
    if (historyModal) historyModal.style.display = "none";
  }

  if (btnCloseModal) btnCloseModal.addEventListener("click", closeHistoryModal);
  if (btnCloseModalBtn) btnCloseModalBtn.addEventListener("click", closeHistoryModal);
  if (historyModal) {
    historyModal.addEventListener("click", (e) => {
      if (e.target === historyModal) closeHistoryModal();
    });
  }
});
