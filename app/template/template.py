from app.utils.url.url import scrape_stripe_treasury_marketing_policy

rag_compliance_template = (
    "As the Marketing Compliance Policy Specialist, your crucial role involves ensuring that all marketing activities strictly adhere to the Stripe compliance policy, meticulously following both regulatory standards and organizational policies. Please analyze the text below and identify the phrases that comply with our Stripe compliance policy on information handling. \n\n{query_str}"
)

rag_non_compliance_template = (
    "As the Marketing Compliance Policy Specialist, your crucial role involves ensuring that all marketing activities strictly adhere to the Stripe compliance policy, meticulously following both regulatory standards and organizational policies. Please analyze the text below and identify the phrases that do not comply with our Stripe compliance policy on information handling. \n\n{query_str}"
)

rag_suggestion_template = (
    "As the Marketing Compliance Specialist, review the following phrases that currently do not comply with the Stripe compliance policy. Provide thoughtful suggestions on how to rephrase each phrase, ensuring compliance with the Stripe policy on information handling. Your expertise is crucial in aligning these expressions with regulatory standards and organizational policies.\n\n{query_str}"
)

zero_shot_compliance_template = template = (
    """
    {context_str}
    ---------------
    As the Marketing Compliance Specialist, review the following text and identify any phrases that do not comply with the provided compliance guidelines.

    {query_str}
    """
)