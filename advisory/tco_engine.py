import argparse

class EnterpriseTCOCalculator:
    """
    Senior AI Advisor tool to calculate Total Cost of Ownership for GPU clusters.
    Factors in CapEx, OpEx, and power consumption for a 3-year projection.
    """
    def __init__(self, gpu_count: int, server_unit_cost: float, power_rate: float):
        self.gpu_count = gpu_count
        self.server_unit_cost = server_unit_cost
        self.power_rate = power_rate # $/kWh

    def calculate_3yr_tco(self, power_consumption_watts: float = 700):
        capex = self.server_unit_cost * (self.gpu_count / 8) # Assuming 8-GPU nodes
        
        # Calculate daily/yearly power cost
        daily_kwh = (power_consumption_watts * 24) / 1000
        annual_power_cost = daily_kwh * 365 * self.power_rate * (self.gpu_count / 8)
        
        # Include maintenance and software (NVIDIA AI Enterprise)
        annual_opex = annual_power_cost + (capex * 0.15) # 10% maintenance + licensing
        
        total_3yr_cost = capex + (annual_opex * 3)
        
        return {
            "CapEx": capex,
            "Annual_OpEx": annual_opex,
            "Total_3Yr_TCO": total_3yr_cost,
            "Cost_Per_GPU_Day": total_3yr_cost / (3 * 365 * self.gpu_count)
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu_count", type=int, required=True)
    parser.add_argument("--server_cost", type=float, required=True)
    parser.add_argument("--power_kwh", type=float, default=0.12)
    args = parser.parse_args()

    tco = EnterpriseTCOCalculator(args.gpu_count, args.server_cost, args.power_kwh)
    report = tco.calculate_3yr_tco()

    print("========================================")
    print("STRATEGIC TCO REPORT (3-YEAR PROJECTION)")
    print("========================================")
    for k, v in report.items():
        print(f"{k:20}: ${v:,.2f}")
    print("========================================")
