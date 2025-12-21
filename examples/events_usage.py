"""Example for listening to model moving events in VTube Studio."""

import asyncio
from vtpy import VTS
from vtpy.data.events import (
    EventType,
    ModelMovedEvent,
    ModelMovedEventSubscriptionRequestData,
    ModelMovedEventSubscriptionRequestConfig,
)
from vtpy.data.common import ErrorData
from vtpy.error import VTSRequestError


async def on_model_moved(event: ModelMovedEvent) -> None:
    """Handle model moved events."""
    data = event.data
    position = data.modelPosition

    print(f"\n=== Model Moved Event ===")
    print(f"Model ID: {data.modelID}")
    print(f"Model Name: {data.modelName}")
    print(f"Position X: {position.positionX:.2f}")
    print(f"Position Y: {position.positionY:.2f}")
    print(f"Rotation: {position.rotation:.2f}°")
    print(f"Size: {position.size:.2f}")


async def main():
    """Main function demonstrating model moved event listening."""
    # Initialize VTS client
    vts = VTS(plugin_name="ExamplePlugin", plugin_developer="ExampleDeveloper")

    try:
        # Connect to VTube Studio at port 8001 and authenticate
        print("Connecting to VTube Studio at localhost:8001...")
        auth_token = await vts.start(host="localhost", port=8001, save_auth_token=False)
        print(f"Successfully authenticated! Token: {auth_token[:20]}...")

        # Register event handler for model moved events
        print("\nRegistering handler for model moved events...")
        vts.on_event(EventType.ModelMovedEvent, on_model_moved)

        # Subscribe to model moved events
        print("Subscribing to model moved events...")
        data = ModelMovedEventSubscriptionRequestData(
            subscribe=True, config=ModelMovedEventSubscriptionRequestConfig()
        )
        subscription_response = await vts.event_sub_model_moved(data)

        # Keep the connection alive and listen for events
        try:
            print("Listening for model moved events. Press Ctrl+C to stop...")
            await asyncio.Event().wait()  # Wait indefinitely
        except KeyboardInterrupt:
            print("\n\nStopping...")

    except ConnectionError as e:
        print(f"Connection error: {e}")
        print("Make sure VTube Studio is running and the WebSocket API is enabled.")
    except ValueError as e:
        print(f"Authentication error: {e}")
        print("You may need to approve the authentication request in VTube Studio.")
    except VTSRequestError as e:
        print(f"VTube Studio Request error: {e}")
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
