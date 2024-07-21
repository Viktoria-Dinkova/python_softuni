from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPE = {"PremiumInfluencer": PremiumInfluencer,
                             "StandardInfluencer": StandardInfluencer
                             }
    VALID_CAPMAIGN_TYPE = {"HighBudgetCampaign": HighBudgetCampaign,
                           "LowBudgetCampaign": LowBudgetCampaign
                           }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:
        if influencer_type not in self.VALID_INFLUENCER_TYPE:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self._find_influencer(username)
        if influencer in self.influencers:
            return f"{username} is already registered."

        influencer = self.VALID_INFLUENCER_TYPE[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:
        if campaign_type not in self.VALID_CAPMAIGN_TYPE:
            return f"{campaign_type} is not a valid campaign type."

        if campaign_id in BaseCampaign.UNIQUE_CAMPAIGN_ID:
            return f"Campaign ID {campaign_id} has already been created."

        campaign = self.VALID_CAPMAIGN_TYPE[campaign_type](campaign_id=campaign_id, brand=brand, required_engagement=required_engagement)
        BaseCampaign.UNIQUE_CAMPAIGN_ID.append(campaign_id)
        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._find_influencer(influencer_username)
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign = self._find_campaign(campaign_id)
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)

        return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        dict = {}
        for campaign in self.campaigns:
            camp_type = campaign.__class__.__name__
            if campaign.approved_influencers:
                for influ in campaign.approved_influencers:
                    dict[camp_type] = influ.reached_followers(camp_type)
    def influencer_campaign_report(self, username: str):
        influencer = self._find_influencer(username)
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaign = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = ["$$ Campaign Statistics $$"]
        for cc in sorted_campaign:
            total_followers = sum((i.reached_followers(cc.__class__.__name__) for i in cc.approved_influencers))
            result.append(f"  * Brand: {cc.brand}, Total influencers: {len(cc.approved_influencers)}, Total budget: ${cc.budget:.2f}, Total reached followers: {(total_followers)}")

        return '\n'.join(result)
    ####  helper

    def _find_influencer(self, name) -> BaseInfluencer:
        try:
            return next(filter(lambda i: i.username == name, self.influencers))
        except StopIteration:
            pass

    def _find_campaign(self, _id) -> BaseCampaign:
        try:
            return next(filter(lambda c: c.campaign_id == _id, self.campaigns))
        except StopIteration:
            pass


