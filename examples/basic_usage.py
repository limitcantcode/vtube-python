"""Basic usage example for vtpy - connecting, authenticating, and getting stats."""

import asyncio
from vtpy import VTS
from vtpy.data.requests import StatisticsRequestData
from vtpy.error import VTSRequestError


async def main():
    """Main function demonstrating basic VTS connection and stats retrieval."""
    # Initialize VTS client
    vts = VTS(plugin_name="ExamplePlugin", plugin_developer="ExampleDeveloper")

    try:
        # Connect to VTube Studio at port 8001 and authenticate
        print("Connecting to VTube Studio at localhost:8001...")
        auth_token = await vts.start(host="localhost", port=8001, save_auth_token=False)
        print(f"Successfully authenticated! Token: {auth_token[:20]}...")

        # Get VTube Studio statistics
        print("\nRequesting VTube Studio statistics...")
        stats_response = await vts.request_statistics(StatisticsRequestData())

        # Display statistics
        stats = stats_response.data
        print("\n=== VTube Studio Statistics ===")
        print(f"Version: {stats.vTubeStudioVersion}")
        print(f"Uptime: {stats.uptime} seconds")
        print(f"Framerate: {stats.framerate} FPS")
        print(f"Allowed Plugins: {stats.allowedPlugins}")
        print(f"Connected Plugins: {stats.connectedPlugins}")
        print(f"Started with Steam: {stats.startedWithSteam}")
        print(f"Window Size: {stats.windowWidth}x{stats.windowHeight}")
        print(f"Fullscreen: {stats.windowIsFullscreen}")

    except ConnectionError as e:
        print(f"Connection error: {e}", exc_info=True)
        print("Make sure VTube Studio is running and the WebSocket API is enabled.", exc_info=True)
    except ValueError as e:
        print(f"Authentication error: {e}", exc_info=True)
        print("You may need to approve the authentication request in VTube Studio.", exc_info=True)
    except VTSRequestError as e:
        print(f"VTube Studio Request error: {e}", exc_info=True)
    except Exception as e:
        print(f"Unexpected error: {e}", exc_info=True)
    finally:
        # Clean up connection
        if vts.connected:
            print("\nClosing connection...")
            await vts.close()
            print("Disconnected.")


if __name__ == "__main__":
    asyncio.run(main())
