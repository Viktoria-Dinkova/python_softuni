from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85  # 85%

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign) -> float:
        return campaign.budget * self.INITIAL_PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)
        if campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)
