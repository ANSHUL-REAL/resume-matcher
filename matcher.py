def get_match_score_and_missing(resume, job_description):
    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    matched = resume_words & job_words
    missing = job_words - resume_words

    score = (len(matched) / len(job_words)) * 100 if job_words else 0
    return score, list(missing)
